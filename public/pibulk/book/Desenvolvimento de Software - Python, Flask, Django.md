# Desenvolvimento de Software - Python, Flask, Django

Índice

1) Python - Prof. Paolla Ramos

2) Python Django - Teoria

3) Python Flask - Teoria

APRESENTAçÃo DA AUUX

Olá, galera! Vamos iniciar os estudos sobre o Python!

Pessoal, eu não vou ser aqueles professores clichês que dizem: Esse assunto é muito fácil. Não é muito fácil! O Como diria o magnífico professor Herbert Almeida, não se assustem com o tema ou com o tamanho da aula. É necessário SIM ter conhecimento sobre programação básica. Énecessário assistira aula de Noções de programação do brilhante Prof. Raphael Lacerda,
e caso não entenda algum comando ou algo do tipo, voltar e rever ou assistir às videoaulas.Sugiro também,
sempre que possível, testar os códigos e aprender - não decorar. Por fim, fazer
MUITAS questões.
Porque Python é LÓGICA. É necessário aprender a lógica porque vai cair uma questão em sua prova em que você terá que resolver usando lógica. Não adianta decorar!
Nesta aula, apresento inúmeras palavras-chave, para que vocês possam entender e internalizar o conteúdo de forma mais simples. Aproveitem o material, além dos esquemas,resumos e mnemónicos. Vamos ao que importa! lí x
/ 174

/

Conceitos Básicos

PYTHoN

RELEVÂNCIA EM PROVA: ALTA

Í® python

Pessoal, vamos falar sobre Python! Python é uma linguagem de código aberto, de propósito geral. É uma linguagem de programação de alto nível, ou seja, com sintaxe mais simplificada e próxima da linguagem humana.
Python é uma linguagem de programação orientada a objetos clara e poderosa, comparável a Perl, Ruby, Scheme ou Java.
Alguns dos recursos notáveis do Python:

Assembler

* Usa uma sintaxe elegante, tornando os programas que você escreve mais fáceis de ler.
* É uma linguagem fácil de usar que simplifica o funcionamento do seu programa. Isso torna o Python ideal para desenvolvimento de protótipos e outras tarefas de programação ad-hoc, sem comprometer a capacidade de manutenção.
* Vem com uma grande biblioteca padrão que suporta muitas tarefas comuns de programação, como conectar-se a servidores da Web, pesquisar texto com expressões regulares, lere modificar arquivos.
* O modo interativo do Python facilita o teste de pequenos trechos de código. Há também um ambiente de desenvolvimento empacotado chamado IDLE.
* É facilmente estendido adicionando novos módulos implementados em uma linguagem compilada como C ou C++.
* Também pode ser incorporado em um aplicativo para fornecer uma interface programável.

* Funciona em qualquer lugar, incluindo Mac OS X, Windows, Linux e Unix, com versões não oficiais também disponíveis para Android e iOS.
* É software livre em dois sentidos. Não custa nada baixar ou usar o Python, ou incluí-lo em seu aplicativo. O Python também pode ser livremente modificado e redistribuído porque,embora a linguagem seja protegida por direitos autorais, ela está disponível sob uma licença de código aberto.
Alguns recursos de linguagem de programação do Python são:

* Uma variedade de tipos de dados básicos está disponível: números (ponto flutuante, inteiros longos complexos e de comprimento ilimitado), strings (ambos ASCII e Unicode), listas e dicionários.
* Python suporta programação orientada a objetos com classes e heranças múltiplas.

* O código pode ser agrupado em módulos e pacotes.

* A linguagem suporta a geração e captura de exceções, resultando em um tratamento de erros mais limpo.
* Os tipos de dados são fortemente e dinamicamente tipados. Misturar tipos incompatíveis(por exemplo, tentar adicionar uma string e um número) faz com que uma exceção seja lançada, de modo que os erros são detectados mais cedo.
* Python contém recursos avançados de programação, como geradores e compreensões de lista.
* O gerenciamento automático de memória do Python libera você de ter que alocar e liberar memória manualmente em seu código.
x

/ 174

/

Python é uma linguagem com uma filosofia de simplicidade no seu design, é uma linguagem de código aberto e tem crescido exponencialmente. A própria comunidade oficial da linguagem diz isso: A comunidade do Python é vasta; diversa e visa crescer; Python é aberto.
Além disso, a comunidade cita que ótimos softwares são suportados por ótimas pessoas,
e o Python não é exceção. A base de usuários é entusiasmada e dedicada a difundir o uso doPython por toda parte. A comunidade pode ajudar a apoiar o iniciante, o especialista e contribui para a base de conhecimento de código aberto cada vez maior.
Python é poderoso... e rápido; roda bem com as outras linguagens; roda em todos os lugares(SO...); é amigável e fácil de aprender; é aberto. Essas são algumas das razões pelas quais as pessoas que usam Python preferem não usar mais nada.
Na documentação é possível encontrar documentação desde a versão 2.7 até a 3.12. E
continua evoluindo de forma exponencial.
Python combina um poder notável com uma sintaxe muito clara. Possui módulos,
classes,
exceções, tipos de dados dinâmicos de nível muito alto e tipagem dinâmica. Existem interfaces para muitas chamadas de sistema e bibliotecas, bem como para vários sistemas de janelas. Novos módulos são facilmente embutidos, escritos em C ou C++ (ou outras linguagens,dependendo da implementação escolhida). O Python também pode ser usado como uma linguagem de extensão para aplicativos escritos em outras linguagens que precisam de scripts ou interfaces de automação fáceis de usar.
Tipagem dinâmica é uma característica de determinadas linguagens de programação,
que não exigem declarações de tipos de dados, pois são capazes de escolher que tipo utilizar dinamicamente para cada variável, podendo alterá-lo durante a compilação ou a execução do programa.
/ 174

/

(CEBRASPE - PC PB- 2022) Na linguagem Python, o tipo de uma variável em tempo de execução é definido pelo interpretador pelo recurso denominado a) tipagem dinâmica.
b) modo interativo.

c) sintaxe.

d) interpretação bytecode.

e) empacotamento.

Comentários: Tipagem dinâmica é uma característica de determinadas linguagens de programação, que não exigem declarações de tipos de dados, pois são capazes de escolher que tipo utilizar dinamicamente para cada variável, podendo alterá-lo durante a compilação ou a execução do programa. (Gabarito: Letra A).

Cada linguagem de programação reserva um significado especial a um conjunto fixo de palavras.Essas palavras são chamadas de palavras-chave.

Com palavras-chave, o programador pode emitir comandos para o compilador ou interpretador.Eles permitem que você diga ao computador o que fazer. Sem palavras-chave, o computador não poderia fazer sentido a partir do texto aparentemente aleatório em seu arquivo de código.
Observe que, como as palavras-chave são palavras reservadas, você não pode usá-las como nomes de variáveis. As palavras-chave Python mais importantes são as seguintes:
PALAVRA-CHAVE DESCRIÇÃO

And é um operador lógico. Os operadores lógicos são usados para combinar instruções

AND

condicionais. O valor de retorno será True somente se ambas as instruções retornarem
True, caso contrário retornará False.

AS Usada para criar um alias.

Usada ao depurar o código. Permite testar se uma condição em seu código retorna

ASSERT

True, caso contrário, o programa gerará um AssertionError. Você pode escrever uma mensagem a ser escrita caso o código retorne false
BREAK Usada para quebrar um loop for ou um loop.while

CLASS Usada para criar uma classe. Uma classe é como um construtor de objetos.

CONTINUE Usada para encerrar a iteração atual em um loop for (ou loop while) e continua na próxima iteração.
DEF Usada para criar (ou definir) uma função.

DEL Usada para excluir objetos. Em Python tudo é um objeto, então a palavra-chave dei também pode ser usada para deletar variáveis, listas ou partes de uma lista etc.
ELIF Usada em instruções condicionais (instruções if) e é abreviação de else if.

ELSE com a ramificação "if", tenta as ramificações "elif" e termina com a ramificação "else"
(até ser avaliada como True)

EXCEPT

Usada em blocos try...except. Ele define um bloco de código a serexecutado se o bloco try gerar um erro. Você pode definir blocos diferentes para diferentes tipos de erro e blocos para executar se nada der errado
FALSE A palavra-chave false é um valor booleano e resultado de uma operação de comparação. A palavra-chave false é igual a o (True é igual a 1).
Usada em blocos try...except. Ele define um bloco de código para ser executado

FINALLY

FOR

quando o bloco try...except...else for final. O bloco finally será executado independentemente de o bloco try gerar um erro ou não. Isso pode ser útil para fechar objetos e limpar recursos.
Um loop for é usado para iterar sobre uma sequência (que é uma lista, uma tupla, um dicionário, um conjunto ou uma string). Permite executar um conjunto de instruções,uma vez para cada item de uma lista, tupla, conjunto etc.

for i in [0,1,2]:
print(i)

FROM
GLOBAL

IF

IMPORT

IN

is
LAMBDA

NONE
NONLOCAL

NOT
OR

PASS

RAISE
RETURN

Usada para importar apenas uma seção especificada de um módulo.

Usada para criar variáveis globais em um escopo não global, por exemplo, dentro de uma função.
Usada para criar instruções condicionais (instruções if) e permite que você execute um bloco de código somente se uma condição for True. Use a palavra-chave else para executar o código se a condição for False
Usada para importar módulos.

Retorna Verdadeiro se uma sequência com 0 valor especificado estiver presente no objeto. Exemplo: x in y
Retorna Verdadeiro se ambas as variáveis forem 0 mesmo objeto. Exemplo: x is y

Uma função lambda é uma pequena função anônima. Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.
O objeto Python None, denota falta de valor. Este objeto não tem métodos. É usado para definir um valor nulo ou nenhum valor.
Usada para trabalhar com variáveis dentro de funções aninhadas, onde a variável não deve pertencer à função interna. Use a palavra-chave nonlocal para declarar que a variável não é local.
É um operador lógico. O valor de retorno será True se a(s) instrução(ões) não forem
True, caso contrário retornará False.

É um operador lógico Os operadores lógicos são usados para combinar instruções condicionais. O valor de retorno será True se uma das instruções retornar True, caso contrário retornará False.
Usada como um espaço reservado para código futuro. Quando a instrução pass é executada, nada acontece, mas você evita obter um erro quando o código vazio não é permitido. Código vazio não é permitido em loops, definições de função, definições de classe ou em instruções if.
Usada para gerar uma exceção. Você pode definirque tipo de erro gerare 0 texto a ser impresso para o usuário.
Sai de uma função e retornar um valor.

(Profs. Paolla Ramos e Raphael L

Valor booleano e resultado de uma operação de comparação. A palavra-chave True é igual a 1 ( False é igual a o).
Usada em blocos try...except. Ele define um bloco de teste de código se ele contém algum erro. Você pode definir blocos diferentes para diferentes tipos de erro e blocos para executar se nada der errado.
Com o loop while podemos executar um conjunto de instruções desde que uma condição seja verdadeira. O loop while requer que as variáveis relevantes estejam prontas (veja que é necessário declarar e atribuir o valor da variável j no exemplo abaixo).
j = o while j < 3:
print(j)
j=j + i

Usado para simplificar 0 tratamento de exceções
Para finalizar uma função, retorna um gerador

Pessoal, nessa aula vamos ver muitos exemplos, é importante mencionar que vários exemplos dessa aula foram retirados ou inspirados em exemplos do W3Tutorials(www.w3schools.com/python). Fizemos isso por dois motivos: (1) os exemplos são excelentes; (2)essa é uma das fontes de inspiração das bancas. Caso você tenha alguma dúvida ou vontade de se aprofundar e testar os programas, você pode usar o https://www.w3schools.com/python/trypython Msp?filename=demo_default o link
QQ

Principais Características

Python é conhecida como uma linguagem de aspectos bastante interessantes e de fácil aprendizagem. O objetivo inicial da linguagem era permitir código enxuto e menos verboso, ou seja, com menos caracteres especiais, menos sintaxes complexas e mais estruturas de código simples. Por isso, se destaca
* Afacilidade para aprender, ler e compreender;

* Ser multiplataforma;

* Possuir modo interativo;

* Usa indentação para marcação de blocos;

* Quase nenhum uso de palavras-chave associadas com compilação;

* Possuir coletor de lixo para gerenciar automaticamente o uso de memória;

* Programação orientada a objetos;

* Programação funcional; e

* Uma imensidão de módulos de extensão, os quais permitem expandir o poder da linguagem
Python.

O Python foi projetado para facilitar a leitura e possui algumas semelhanças com o idioma inglês com influência da matemática. Python usa novas linhas para completar um comando, ao contrário de outras linguagens de programação que geralmente usam ponto e vírgula ou parênteses. Alinguagem depende de recuo (indentação), usando espaço em branco, para definir o escopo; como o escopo de loops, funções e classes. Outras linguagens de programação costumam usar colchetes para essa finalidade.
Python é uma linguagem de programação interpretada, isso significa que, como desenvolvedor,você escreve arquivos Python (.py) em um editor de texto e depois coloca esses arquivos no interpretador python para serem executados.
A maneira de executar um arquivo python é assim na linha de comando:
C:\Users\Your Namexpython helloworld.py

Em que "helloworld.py" é o nome do seu arquivo python.

/ 174

/

Sintaxe do Python

A sintaxe do Python pode ser executada escrevendo diretamente na linha de comando:

>>> print("Hello, World!")
Hélio, World!

O recuo, ou indentação, refere-se aos espaços no início de uma linha de código. Em outras linguagens de programação, o recuo no código é apenas para legibilidade, o recuo emPython é muito importante. Python usa recuo para indicar um bloco de código.
if 5 > 2:

print("Cinco é maior que dois!")

O número de espaços fica a seu critério como programador, o uso mais comum é quatro,
mas tem que ser pelo menos um.
if 5 > 2:

print("Cinco é maior que dois!")
if 5 > 2:

print("Cinco é maior que dois!")

Você precisa usaro mesmo número de espaços no mesmo bloco de código, caso contrário,
o Python fornecerá um erro: IndentationError: unexpected indent
*

Variáveis em Python

Variáveis são contêineres para armazenarvalores de dados. Python não tem comando para declarar uma variável. Em Python, as variáveis são criadas quando você atribui um valor a ela:
x = 5

y = "HellOj World!"

Python não tem comando para declarar uma variável. As variáveis não precisam ser declaradas com nenhum tipo específico e podem até mudar de tipo depois de terem sido definidas. V
AS VARIÁVEIS NÃO PRECISAM SER DECLARADAS

Se você deseja especificar o tipo de dados de uma variável, isso pode ser feito com conversão.
x = str(3) # x será uma string com valor '3'

y = int(3) # y será um inteiro igual a 3
z = float(3) # será um float de valor igual a 3.0

Você pode obter o tipo de dados de uma variável com a função type().
x = 5

y = "3ohn"

print(type(x))
print(type(y))

Resultará em: <class 'int'> e <class 'str'>. Variáveis de string podem ser declaradas usando aspas simples ou duplas:
x = "Professor"
x = 'Professor'

Python permite atribuir valores a várias variáveis em uma linha, neste caso, cada variável recebe o respectivo valor entre vírgulas:
x, y, z = "Laranja"., "Banana", "Cereja"

Além disso, é possível atribuir o mesmo valor a várias variáveis em uma linha, vai que você precisa,não é? @

/ 174

/

x = y = z = "Laranja"

Python, assim como Java, é case sensitive, ou seja, os nomes de variáveis diferenciam maiusculas de minúsculas.
a = 4

A = "Professor"

Uma variável pode ter um nome curto (como x e y) ou um nome mais descritivo (idade,volume_total, marca_veiculo). Vejamos as regras para nomes de variáveis Python:

* Um nome de variável deve começar com uma letra ou o caractere sublinhado

* Um nome de variável não pode começar com um número

* Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (Az, 0-9
e_)

* Os nomes das variáveis diferenciam maiúsculas de minúsculas (idade, idade e IDADE são três variáveis diferentes)
Variáveis criadas fora de uma função (como em todos os exemplos acima) são conhecidas como variáveis globais. As variáveis globais podem ser usadas por todos, tanto dentro das funções quanto fora delas.
x = "incrível"
def myfunc():

print("Python é " + x)
myfunc()

Vocês viram, nesse exemplo, que usamos uma concatenação dentro do print. Aconcatenação pode ser definida como a integração de duas strings em um objeto. Em Python, você pode executar a concatenação usando o operador +. (tí
/ 174

/

Se você criar uma variável com o mesmo nome dentro de uma função, essa variável será local e só poderá ser usada dentro da função. A variável global com o mesmo nome permanecerá como estava, global e com o valor original.
x = "incrível"
def myfunc():

x = "fantástico"
print("Python é " + x)

myfunc()
print("Python é " + x)

A primeira variável x terá o valor "Incrível". Já a segunda - dentro da função myfunc - possui o valor"fantástico". Assim, no print dentro da função myfunc receberemos a mensagem:
Python é fantástico. Já fora da função, na última linha do exemplo, o print vai gerar a mensagem: Python é incrível. Ficou claro? r.
Normalmente, quando você cria uma variável dentro de uma função, essa variável é local e só pode ser usada dentro dessa função. Para criar uma variável global dentro de uma função, você pode usar a palavra-chave global.
Global: Usada para criar variáveis globais em um escopo não global, por exemplo,
dentro de uma função.
def myfunc():
global x x = "fantastic"
Tipos de dados Python

Na programação, o tipo de dados é um conceito importante. Variáveis podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer coisas diferentes. O Python tem os seguintes tipos de dados integrados por padrão, nestas categorias:
TIPO DE DADO DESCRIÇÃO
EXEMPLO

TEXTO str x = "Hello
World"

Int: x = "Hello World"

NUMÉRICOS int, float, complex

SEQUÊNCIA list, tupla, range

Float: x= 20.5
Complex: x = ij

List: x = ["maçã", "banana", "cereja"]

Tupla: x = ("maçã", "banana", "cereja")
Range: x = range(6)

MAPEAMENTO dict
Dict: x = ("nomw=e": "John", "idade": 36}

Set: x = {"maçã", "banana", "cereja"}

CONJUNTO set,frozenset

Frozenset: x = frozenset({"maçã",
"banana", "cereja"})

BOOLEANO bool x = True

Bytes: x = b"Hello"

BINÁRIO bytes, bytearray, memoryview

Bytearray: x = bytearray(s)
Memoryview: x = memoryview(bytes(5))

NENHUM TIPO NoneType NoneType:
x = None

Pode haver momentos em que você deseja especificar um tipo para uma variável. Isso pode serfeito com casting. Python é uma linguagem orientada a objetos e, como tal, usa classes para definirtipos de dados, incluindo seus tipos primitivos. A conversão em python é, portanto, feita usando funções construtoras:
int() - constrói um número inteiro a partir de um literal inteiro, um literal float
(removendo todos os decimais) ou um literal de string (desde que a string represente um número inteiro)
float() - constrói um número float a partir de um literal inteiro, um literal float ou um literal de string(desde que a string represente um float ou um inteiro)

str() - constrói uma string a partir de uma ampla variedade de tipos de dados,
incluindo strings,
literais inteiros e literais float

Strings podem conter uma ou mais linhas, veja um exemplo de uma string com mais de uma linha usando três aspas - três aspas duplas () ou três aspas simples ('"):
/ 174

/

a = """Estratégia Concursos é referência na preparação de alunos para ConcursosPúblicos. Para ser aprovado em um concurso público, você precisa estudar com estratégia print(a)
Strings em Python

Como muitas outras linguagens de programação populares, strings em Python são arrays de bytes que representam caracteres unicode. No entanto, o Python não possui um tipo de dados de caractere, um único caractere é simplesmente uma string com um comprimento de 1.Colchetes podem ser usados para acessar elementos da string.
a = "Hello, World!"
print(a[l])

No exemplo, o resultado será "e" porque o array inicia em o(zero). Como strings são arrays,
podemos fazer um loop pelos caracteres em uma string, com um loop for.

for x in "banana":
print(x)

Para obter o comprimento de uma string, use a função len().

a = "Hello, World!"
print(len(a))

Para verificar se uma determinada frase ou caractere está presente em uma string,
podemos usar a palavra-chave in.
txt = "Estratégia Concursos é referência na preparação de alunos
"
print("Concursos" in txt)

É possível procurar uma palavra em uma instrução if. Vejamos um exemplo:

txt = "Estratégia Concursos é referência na preparação de alunos
"
if "Estratégia" in txt:

print("Sim!, Estratégia está presente no texto.")

Há muitas funções que podem ser realizadas ou utilizadas em strings. É
possível retornar um intervalo de caracteres usando a sintaxe de slice. Slice consiste em "fatiar", ou seja, cortar uma
*

parte da string. É necessário especificar o índice inicial e o índice final, separados por dois pontos,
para retornar uma parte da string.

b = "Estratégia Concursos!"
print(b[2:5])

Esse exemplo retorna "tra". Importante que vocês entendam que o corte final desconsidera o conteúdo do índice final, perceba que (b[s]) = t. Esse valor não é retornado.
Ao omitir o índice inicial, o intervalo começará no primeiro caractere:

b = "Estratégia Concursos!"
print(b[:10])

Esse exemplo retorna apenas o texto "Estratégia". Por outro lado, ao omitir o índice final , o intervalo irá para o final:
b = "Estratégia Concursos!"
print(b[ll:])

Esse exemplo retorna apenas o texto " Concursos!". Outra forma de cortar a string é utilizando índices negativos. É possível usar índices negativos para iniciar o corte a partir do final da string:
b = "Estratégia Concursos!"
print(b[-10])

O exemplo acima retorna apenas o texto "C".

Vejamos agora uma lista de métodos integrados disponíveis no Python que você pode usar em strings.
(FGV - MPE GO- 2022) Assinale a lista de números produzida pela execução, na IDLE
Shell 3.9.9, do código Python a seguir.

forx in range(-i, -10, -1):
print (x)

a) -1-2-3-4-5-6-7-8-9

b) -9 -8 -7-6-5 -4 -3-2-1

c) 0-1-2-3 -4 -5-6-7-8 -9

d) 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

e) -1 -2 -3 -4 -5 -6 -7 -8 -9 -10.

/ 174

/

Comentários: Pessoal, as bancas gostam muito de índices negativos, para dificultar um pouco. No caso da questão, é gerada uma sequência de números negativos iniciando em -1 e parando antes do -10 (ou seja, o for para no-9). O For é incrementado de -iem -1 formando a sequência -1-2 -3 -4-5-6 -7 -8 -9. (Gabarito: Letra A)
MÉTODOS PARA MODIFICAR

STRINGS

UPPERO Retorna a string em maiusculas

LOWERl] Retorna a string em letras minúsculas

DESCRIÇÃO

STRIPO Remove qualquer espaço em branco do início ou do fim

REPLACEU Substitui uma string por outra string. Ex: replaceCh", "j")

SPLITO Retorna uma lista em que 0 texto entre 0 separador especificado se torna os itens da lista.
É possível, também, formatar strings. podemos combinar strings e números usando o método format()! lí O método format() pega os argumentos passados, os formata e os coloca na string onde estão os espaços reservados posicao = 01
txt = "0 Estratégia Concursos é uma fabrica de {}"
print(txt.format(posicao))

O método formatO recebe um número ilimitado de argumentos e são colocados nos respectivos espaços reservados:
vagas = 431

orgao = "SEFA MG"
cargo = "Auditor Fiscal"

concursos = "Há {} vagas no concurso {} para {}."
print(concursos.format(vagas, orgao, cargo))

Para inserir caracteres ilegais em uma string, use um caractere de escape.

Um caractere de escape é uma barra invertida \seguida pelo caractere que você deseja inserir.

Um exemplo de um caractere ilegal é uma aspas dupla dentro de uma string que é cercada por aspas duplas: txt = " O Estratégia Concursos é uma "fabrica" de ois.". Você receberá um erro se usar aspas duplas dentro de uma string cercada por aspas duplas. Para corrigir esse problema, use o caractere de escape \", da seguinte forma: txt = "O Estratégia Concursos é uma \"fabrica\" de ois."
*

CARACTER DE ESCAPE DESCRIÇÃO

V Aspas simples

\\ Barra invertida

\N Nova linha

\R Volta para margem esquerda e em uma nova linha

\T Tab

\B Backspace

\F Caractere de controle ASCII de quebra de página. Ele força a impressora a ejetar a página atual e a continuar imprimindo na parte superior de outra.
\000 Valor octal

\XHH Valor hexadecimal

Python tem um conjunto de métodos integrados que você pode usar em strings.

FUNÇÃO DESCRIÇÃO

CAPITALIZEI)
CASEFOLDO

B6D

COUNTl]
ENCODEO
ENDSWITHl]
EXPANDTABSÍ)

FÍNDõ
FORMATO
FORMALMAPÍ]

INDEXO
ISALNUMO
ISALPHAO
ISASCIIO
ISDECIMALO
ISDIGITO
ISIDENTIFIERO
ISLOWERO

204013

Converte o primeiro caractere em maiúscula
Converte string em minúsculas

Retorna uma string centralizada

Retorna o número de vezes que um valor especificado ocorre em uma string
Retorna uma versão codificada da string

Retorna verdadeiro se a string terminar com o valor especificado
Define o tamanho da guia da string

Pesquisa a string por um valor especificado e retorna a posição de onde foi encontrado
Formata valores especificados em uma string

Formata valores especificados em uma string

Pesquisa a string por um valor especificado e retorna a posição de onde foi encontrado
Retorna True se todos os caracteres da string forem alfanuméricos

Retorna True se todos os caracteres da string estiverem no alfabeto
Retorna True se todos os caracteres da string forem caracteres ASCII
Retorna True se todos os caracteres na string forem decimais
Retorna True se todos os caracteres da string forem dígitos

Retorna True se a string for um identificador

Retorna True se todos os caracteres da string forem minúsculos
Retorna True se todos os caracteres da string forem numéricos

ISPRINTABLEÍl Retorna True se todos os caracteres da string forem imprimíveis
ISSPACEU Retorna True se todos os caracteres na string forem espaços em branco
ISTITLEO Retorna True se a string seguiras regras de um título

ISUPPERU Retorna True se todos os caracteres da string forem maiúsculos

JOINO Converte os elementos de um iterável em uma string
LJUSTIJ Retorna uma versão justificada à esquerda da string
LOWERd Converte uma string em letras minúsculas

LSTRIPO Retorna uma versão de corte à esquerda da string

MAKETRANSU Retorna uma tabela de tradução para ser usada nas traduções

PARTITIONl] Retorna uma tupla onde a string é dividida em três partes

REPLACEÍJ Retorna uma string onde um valor especificado é substituído por um valor especificado

RFINO[] Pesquisa a string por um valor especificado e retorna a última posição de onde foi encontradoRINDEXO Pesquisa a string por um valor especificado e retorna a última posição de onde foi encontradoRJUSTU Retorna uma versão justificada à direita da string

RPARTITIONl] Retorna uma tupla onde a string é dividida em três partes
RSPLITU Divide a string no separador especificado e retorna uma lista
RSTRIPU Retorna uma versão de corte à direita da string

SPLITU Divide a string no separador especificado e retorna uma lista
SPLITLINESU Divide a string nas quebras de linha e retorna uma lista
STARTSWITHO Retorna verdadeiro se a string começar com o valor especificado

STRIPÜ Remove espaços em branco (ou caracteres dentro do parêntese) do início/fim da string

SWAPCASEl) Troca de maiúsculas, minúsculas tornam-se maiúsculas e vice-versa

TITLEO Converte o primeiro caractere de cada palavra para maiúscula

TRANSLATEl] Retorna uma string traduzida

UPPERtl Converte uma string em maiúscula

ZFILLH Preenche a string com um número especificado de valores o no início

Booleanos em Python

Booleanos representam um dos dois valores: True ou False. Na programação, muitas vezes você precisa saber se uma expressão é True ou False. Você pode avaliar qualquer expressão em Python e obter uma das duas respostas. Quando você compara dois valores, a expressão é avaliada e oPython retorna a resposta booleana:

print(10 > 9) #Retorna True

/ 174

/

print(10 == 9)#Retorna False print(10 < 9) #Retorna False
Curiosidades: A função bool() permite avaliar qualquer valor e dar a você True ou
False em troca. A
maioria dos valores são verdadeiros. Quase qualquer valor é avaliado True se tiver algum tipo de conteúdo. Qualquer string é True, exceto strings vazias. Qualquer número é True, exceto o (zero).Qualquer lista, tupla, conjunto e dicionário são True, exceto os vazios.

Por outro lado, há valores avaliados como False, exceto valores vazios, como (), [],
{},"", o número o e o valor None. E, claro, o valor False é avaliado como False. Exemplos de valores avaliados comoFalse:

bool(False)
bool(None)
bool(0)
bool("")

bool(())

bool([])

bool({})

Operadores Python

Os operadores são usados para realizar operações em variáveis e valores.
Python divide os operadores nos seguintes grupos:
* Operadores aritméticos

* Operadores de atribuição

* Operadores de comparação

* Operadores lógicos

* Operadores de identidade

* Operadores de associação

* Operadores bit a bit
Operadores aritméticos Python

/ 174

/

Exponenciação

Floor Division: arredonda o resultado para número inteiro mais próximo x**yO X // y

Os operadores de atribuição são usados para atribuir valores a variáveis:

Igual x==y

Diferente x != y

Maior que x > y

Menorque x < y

Maior ou igual a x >= y

Menorou igual a x <= y

Os operadores lógicos são usados para combinar instruções condicionais:

OPERADOR DESCRIÇÃO
EXEMPLO

AND Retorna True se ambas as declarações forem verdadeiras x < 5 and x < io

OR
NÕT

Retorna True se uma das declarações for verdadeira

Inverte o resultado, retorna False se o resultado for verdadeiro x < 5 orx < 4
not(x < 5 and x < io)

Os operadores de identidade são usados para comparar os objetos, não se forem iguais,
mas se forem realmente o mesmo objeto, com a mesma localização de memória:
OPERADOR DESCRIÇÃO
EXEMPLO

IS Retorna True se ambas as variáveis forem 0 mesmo objeto x is y

ISNOT Retorna True se ambas as variáveis não forem 0 mesmo objeto x is not y

Os operadores de associação são usados para testar se uma sequência é apresentada em um objeto:

OPERADOR DESCRIÇÃO
EXEMPLO

Retorna True se uma sequência com o valor especificado estiver x in y presente no objeto
Retorna True se uma sequência com o valor especificado não xnotiny estiver presente no objeto
Operadores Bitwise Python: Operadores bit a bit são usados para comparar números (binários):

DESCRIÇÃO

Define cada bit como i se ambos os bits forem i
Define cada bit como i se um dos dois bits for i

Define cada bit como i se apenas um dos dois bits for i
Inverte todos os bits

Desloque para a esquerda empurrando zeros da direita e deixe os bits mais à esquerda fora
Desloque para a direita empurrando cópias do bit mais à esquerda da esquerda e deixe os bits mais à direita fora
Pessoal, para tentar explicar melhor, vamos a um exemplo. Suponha: x « y. Isso retorna "x" com os seus bits movidos "y" casas à esquerda, adicionando zeros aos bits "novos" da direita. Isso é a mesma coisa que multiplicar x por 2**y. Exemplo: 14 « 9 # decimal 7168.1110 « 1001# binário
1110000000000

Por outro lado, vejamos o ». x » y retorna "x" com seus bits movidos "y" casas à direita. Isso é o mesmo que x // 2 ** y. Exemplo: 14 » 9 # decimal 0 2 » 1 #decimal 1. 1110 » 1001 #binário 0

10 » 1 # binário 1

Coleções em Python

Listas Python

As listas são usadas para armazenarvários itens em uma única variável. As listas são um dos ^tipos de dados internos do Python usados para armazenar coleções de dados, os outros 3 sãoTupla ,
Conjunto e Dicionário, todos com qualidades e usos diferentes. As listas são criadas usando colchetes:
listai = ["maçã", "banana", "cereja"]
print(listal)

Os itens da lista são ordenados, alteráveis e permitem valores duplicados. Os itens da lista são indexados, o primeiro item possui índice [o], o segundo item possui índice [1], etc.Quando dizemos que as listas estão ordenadas, significa que os itens têm uma ordem definida, e essa ordem não será alterada. Se você adicionar novos itens a uma lista, os novos itens serão colocados no final da lista.
A lista é mutável, o que significa que podemos alterar, adicionar e remover itens em uma lista após ela ter sido criada. Como as listas são indexadas, as listas podem ter itens com o mesmo valor:
(CESPE - DPE RO - 2022) Na linguagem Python, são consideradas sequências mutáveis as:
a) strings b) cadeias c) tuplas d) listas e) ranges.
Comentários: A lista é mutável, o que significa que podemos alterar, adicionar e remover itens em uma lista após ela ter sido criada. Portanto, as listas são consideradas sequências mutáveis. (Gabarito: Letra D).
Iista2 = ["maçã", "banana", "cereja", "maçã", "cereja"]
print(lista2)

Para determinar quantos itens uma lista possui, use a função len():
lista3 = ["maçã", "banana", "cereja"]

print(len(lista3))

Os itens da lista podem ser de qualquertipo de dados:

/ 174

/

listai = ["maçã", "banana", "cereja"]
lista2 = [1, 5, 7, 9, 3]

lista3 = [True, False, False]

Uma lista pode conter diferentes tipos de dados:

listai = ["abc", 34, True, 40, "masculino"]

Da perspectiva do Python, as listas são definidas como objetos com o tipo de dados '
I ist'. Também é possível usar o construtor Iist() ao criar uma nova lista.
Coleções Python (matrizes)

Existem quatro tipos de dados de coleção na linguagem de programação Python:

* Lista é uma coleção que é ordenada e mutável. Permite membros duplicados.

* Tupla é uma coleção ordenada e imutável. Permite membros duplicados.

* Set é uma coleção não ordenada, imutável1 e não indexada. Nenhum membro duplicado.

* Dicionário é uma coleção ordenada2 e mutável. Nenhum membro duplicado.

Ao escolher um tipo de coleção, é útil entender as propriedades desse tipo. Escolher o tipo certo para um determinado conjunto de dados pode significar retenção de significado e pode significar um aumento na eficiência ou segurança.
Vejamos agora como os itens da lista são indexados e você pode acessá-los consultando o número do índice:
listai = ["maçã", "banana", "cereja"]
print(listal[l]) #imprime na tela banana.

Por outro lado, a indexação negativa significa começar do fim. -i refere-se ao último item, ^refere-se ao penúltimo item etc.

listai = ["maçã", "banana", "cereja"]
print(listal[-1]) #imprime na tela cereja.

Os itens do conjunto são imutáveis, mas você pode remover e/ou adicionar itens sempre que quiser.

A partir da versão 3.7 do Python, os dicionários são ordenados. No Python 3.6 e anteriores, os dicionários não são ordenados.
/ 174

/

Você pode especificar um intervalo de índices especificando onde começar e onde terminar o intervalo. Ao especificar um intervalo, o valor de retorno será uma nova lista com os itens especificados.
listai = ["maçã", "banana" "cereja", "laranja", "kiwi",
print(listal [2:5]) #imprime na tela ['cereja', 'laranja'

"melão",

, 'kiwi']

"manga"]

Isso retornará os itens da posição 2 até a posição 5. Lembre-se que o primeiro item é a posição o(zero), e note que o item na posição 5 NÃO está incluído
Para determinar se um item especificado está presente em uma lista, use a palavra-chave in:
listai = ["maçã", "banana", "cereja"]
if "maçã" in listai:

print("Sim, 'maçã' é uma fruta da lista")

Para alterar o valor de um item específico, consulte o número do índice:
listai = ["maçã", "banana", "cereja"]

listai [1] = "abacaxi"

print(listal) #imprime ['maçã', 'abacaxi', 'cereja']

Para alterar o valor dos itens dentro de um intervalo específico, defina uma lista com os novos valores e consulte o intervalo de números de índice onde deseja inserir os novos valores:
listai = ["maçã", "banana", "cereja", "laranja", "kiwi",
"manga"]
listal[l:3] = ["abacaxi", "melancia"]

print(listal) #imprime ['maçã', 'abacaxi', 'melancia',
'laranja', 'kiwi',
'manga']

Python tem um conjunto de métodos embutidos que você pode usar em listas/matrizes.

MÉTODO DESCRIÇÃO

APPENDO Adiciona um elemento no final da lista
CLEARO Remove todos os elementos da lista
COPYO Retorna uma cópia da lista

COUNTO Retorna o número de elementos com o valor especificado

EXTENDÍ) Adiciona os elementos de uma lista (ou qualquer iterável)z ao final da lista atual

INDEXO Retorna o índice do primeiro elemento com o valor especificado

INSERTO Adiciona um elemento na posição especificada

POPO Remove o elemento na posição especificada

/ 174

/

Remove o primeiro item com o valor especificado
Inverte a ordem da lista

Inverte a ordem da lista

(FGV- MPE SC - 2022) Analise o código Python a seguir.
xi = {"A", "B", "C"}

X2 = ["AA", "BB", "CC"]

xi.add("B")

x2.append("BB")
x2.append(xi)
print (x2)

Dado que os elementos de xi podem ser exibidos em ordem aleatória, a linha que possivelmente é produzida pelo comando print na execução do código acima é:
a) ['AA', 'BB', 'CC, 'BB', {'C, 'A', 'B'}]

b) ['AA', 'BB', 'CC, 'BB', 'C, 'A', 'B', 'B']

c) ['AA', 'BB', 'CC, 'BB', 'C, 'A', 'B']

d) ['AA', 'BB', 'CC, ['BB'], {'B'}]

e) {'AA','BB','CC,'BB','C, 'A','B'}

Comentários: Pessoal, primeiramente devemos desconsiderar xi já que 0 comando da questão diz que os elementos de xi podem ser exibidos em ordem aleatória. Vejamos então a ordem de X2. Inicialmente temos um ["AA","BB", "CC"] que consiste no X2 original. Após, teremos BB (devido ao X2.append ("BB")). Portanto ficamos com 'AA1, 'BB1,'CC, 'BB'. Dessa forma ficamos entre as opções a,b, cee. Porém, depois do X2 há um xi (x2.append(xi)). Dessa forma, podemos ter um["A", "B", "C"} em uma sequência aleatória - como diz 0 comando da questão. A única opção que possui um {"A", "B", "C"} em sequência aleatória é a letra A. (Gabarito: Letra A).
Você pode percorrer os itens da lista usando um loop for:

listai = ["maçã", "banana", "laranja"]
for x in listai:

print(x)

Além disso, é possível percorrer os itens da lista consultando seu número de índice.
Use as funções range() e len() para criar um iterável adequado.
listai = ["maçã", "banana", "laranja"]
for i in range(len(listal)):

print(listal[i])

/ 174

/

Outra forma de percorrer a lista é usando um loop while. Use a função len() para determinar o comprimento da lista, então comece em o e faça um loop pelos itens da lista consultando seus índices. Lembre-se de aumentar o índice em 1 após cada iteração.
listal= ["maçã", "banana", "laranja"]
i = 0

while i < len(listal):
print(listal[i])

i = i + 1

/ 174

/

List Comprehension

O List Comprehension oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente. Por exemplo, com base em uma lista de frutas, você deseja uma nova lista, contendo apenas as frutas com a letra "a" no nome. Sem compreensão de lista, você terá que escrever uma declaração for com um teste condicional dentro:
frutas = ["maçã", "banana", "laranja", "kiwi", "mango"]
novalista = []

for x in frutas:
if "a" in x:

novalista.append(x)
print(novalista)

Com List Comprehension, você pode fazertudo isso com apenas uma linha de código:

frutas = ["maçã", "banana", "laranja"]
novalista = [x for x in frutas if "a" in x]

vejamos agora como Classificar lista alfanumérica. Objetos de lista possuem um método sort() que ordenará a lista de forma alfanumérica, em ordem crescente, por padrão:frutas.sort()

para classificar de forma decrescente, use reverse = True frutas.sort(reverse = True)
Agora vejamos como é possível copiar uma lista! Você não pode copiar uma lista simplesmente digitando Iist2 = listi, porque: Iist2 será apenas uma referência a listi, e as alterações feitas listi automaticamente também serão feitas em Iist2. Existem maneiras de fazer uma cópia, uma delas é usar o método interno copy().
frutas = ["maçã", "banana", "laranja"]
minhalista = frutas.copy()

print(minhalista)

Outra maneira de fazer uma cópia é usar o método interno Iist().
frutas = ["maçã", "banana", "laranja"]

/ 174

/

minhalista = list(frutas)
print(minhalista)

Existem várias maneiras de unir ou concatenar duas ou mais listas em Python. Uma das maneiras mais fáceis é usando o operador +.
listai = ["a", "b", "c"]
lista2 = [1, 2, 3]

lista3 = listai + lista2
print(lista3)

Mais uma maneira de juntar duas listas é anexando todos os itens da Iista2 na listai, um por um:listai = ["a", "b" , "c"]

lista2 = [1, 2, 3]

for x in lista2:
listai.append(x)

print(listal)

Tuplas Python

Tuplas são usadas para armazenar vários itens em uma única variável. Tupla é um dos
4 tipos de dados internos do Python usados para armazenar coleções de dados, os outros 3 sãoList, Set e
Dictionary , todos com qualidades e usos diferentes. Uma tupla é uma coleção ordenada e imutável .Tuplas são escritas com colchetes.
/ 174

/

Os itens de tupla são indexados, o primeiro item possui índice [o], o segundo item possui índice[1], e assim sucessivamente. Quando dizemos que as tuplas estão ordenadas, significa que os itens têm uma ordem definida, e essa ordem não será alterada.
As tuplas são imutáveis, o que significa que não podemos alterar, adicionar ou remover itens após a criação da tupla.
NÃO PODEMOS ALTERAR, ADICIONAR OU REMOVER ITENS
APÓS A CRIAÇÃO DA TUPLA.

Como as tuplas são indexadas, elas podem ter itens com o mesmo valor, ou seja,
tuplas permitem duplicatas.
tuplal = ("maça", "banana", "laranja","maça")

Para determinar quantos itens uma tupla possui, use a função len():

print(len(tuplal))

Os itens de tupla podem ser de qualquertipo de dados:

tuplal = ("maça", "banana", "laranja") #tupla de strings tupla2 = (1, 5, 7, 9, 3) #tupla de inteiros tupla3 = (True, False, False) #tupla de booleanos tupla4 = ("abc", 34, True, 40, "masculino") #tupla de diversos tipos
Na prática, é muito usado, além de necessário, tuplas de diferentes tipos de dados. A
tupla 4
apresenta strings, inteiros e valores booleanos.

Para acessar os itens da tupla, é possível consultar o número do índice, entre colchetes - lembrando que inicia em o (zero):
tuplal = ("maça", "banana", "laranja")
print(tuplal[l]) #imprime banana

Da mesma forma que ocorre na lista, é possível acessar tuplas com índice negativo.
Lembrando que o -1 pega o último item, -2refere-se ao penúltimo item, etc.
tuplal = ("maça", "banana", "laranja")
print(tuplal[-1]) #imprime laranja

As tuplas são imutáveis, o que significa que você não pode alterar, adicionar ou remover itens depois que a tupla for criada. Mas existem algumas soluções alternativas. Uma delas é converter uma tupla em uma lista, alterar a lista e convertê-la novamente em uma tupla. Para excluir completamente uma tupla, pode-se usar a palavra-chave dei.
tuplal = ("maça", "banana", "laranja")
dei tuplal

É possível percorrer os itens da tupla usando um loop for.
tuplal = ("maçã", "banana", "laranja")

for x in tuplal:

print(x)

Pessoal, esse é o exemplo mais simples de todos, e o detalhe é que as questões muitas vezes cobram o loop for, portanto, atenção! Vamos ver mais detalhes quando falarmos sobre o Loop for.
Ademais, é possível percorrer os itens da tupla consultando seu número de índice. Use as funções range()e len() para criar um iterável adequado.
tuplal = ("maçã", "banana", "laranja")
for i in range(len(tuplal)):

print(tuplal[i])

Além do loop for, é possível percorrer os itens da lista usando um loop while. Use a função len()para determinar o comprimento da tupla, então comece em o e faça um loop pelos itens da tupla consultando seus índices. Lembre-se, sempre, de aumentar o índice em 1 após cada iteração.
tuplal= ("maçã", "banana", "laranja")
i = 0

while i < len(tuplal):
print(tuplal[i])

i = i + 1

Além de percorrer as tuplas, é possível concatená-las usando o operador de concatenação
+:
tuplal = ("a", "b" , "c")

tupla2 = (1, 2, 3)

tupla3 = tuplal + tupla2

/ 174

/

print(tupla3)

Há outra função incrível que pode ser utilizada em tuplas! w Se você quiser multiplicar o conteúdo de uma tupla um determinado número de vezes, você pode usar o operador *:
frutas tuplal
("maçã",
frutas *

"banana",

"laranja")

print(tuplal)

## imprime ('maçã', 'banana', 'laranja', 'maçã', 'banana', 'laranja')
Python possui dois métodos integrados que você pode usar em tuplas.

MÉTODO DESCRIÇÃO

COUNTO Retorna o número de vezes que um valor especificado ocorre em uma tupla

INDEXO

Conjuntos Python

Procura na tupla um valor especificado e retorna a posição de onde foi encontrado

Conjuntos, também conhecidos como SETs, são usados para armazenar vários itens em uma única variável. Um conjunto é uma coleção não ordenada, imutável3 e não indexada. São escritos com colchetes.
conjuntol = {"maça", "banana", "cereja"}
print(conjuntol)

Não ordenado significa que os itens em um conjunto não têm uma ordem definida. Os itens do conjunto podem aparecer em uma ordem diferente toda vez que você os usa e não podem ser referenciados por índice ou chave. Imutável significa que não podemos alterar os itens após a criação do conjunto. Os conjuntos não podem ter dois itens com o mesmo valor.
Diferente das listas, e tuplas, os conjuntos não podem ter dois itens com o mesmo valor. Por outro lado, assim como as demais coleções, é possível determinar quantos itens um conjunto possui usando a função len().
Não é possível acessar itens em um conjunto fazendo referência a um índice ou a uma chave.
Mas você pode percorrer os itens do conjunto usando um loop for ou perguntar se um valor especificado está presente em um conjunto, usando a palavra-chave in.
A partir da versão 3.7 do Python, os dicionários são ordenados. No Python 3.6 e anteriores, os dicionários não são ordenados.
/ 174

/

thisset = {"maça", "banana", "cereja"}
for x in thisset:

print(x)

Não é possível alterar itens depois que um conjunto é criado, porém é possível adicionar novos itens. Para adicionar um item a um conjunto, use o método add().
thisset = {"maça", "banana", "cereja"}
thisset.add("laranja")

Para adicionar itens de outro conjunto ao conjunto atual, use o método updateQ.

thisset = {"maça", "banana", "cereja"}
tropical = {"pinemaça", "mango", "papaya"}

thisset.update(tropical)

O objeto no método update() não precisa ser um conjunto, pode ser qualquer objeto iterável
(tuplas, listas, dicionários etc.).

thisset = {"maça", "banana", "cereja"}
mylist = ["kiwi", "laranja"]

thisset.update(mylist)

Para remover um item em um conjunto, use o método remove(), ou .discard(). Se o item a ser removido não existir, usando o método remove(), será gerado um erro. Por outro lado,se o item a ser removido não existir, usando o método discard() NÃO irá gerar um erro.
thisset = {"maça", "banana", "cereja"}
thisset.remove("banana")

Além de remove(), e discard(), é possível usar o método o pop() que irá remover o último item do conjunto. Por fim, o método clear() esvazia o conjunto, e a palavra-chave dei excluirá o conjunto completamente.
Vejamos agora as várias maneiras de unir dois ou mais conjuntos em Python.

*

Você pode usar o método union() que retorna um novo conjunto contendo todos os itens de ambos os conjuntos ou o método update() que insere todos os itens de um conjunto em outro.Ambos union() e update() excluirão quaisquer itens duplicados.

setl = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = setl.union(set2)
setl.update(set2)

Python é tão incrível que há vários métodos para trabalhar com conjuntos.
Vejamos agora os métodos intersection(), intersection_update(),symmetric_difference(), e symmetric_difference_update().
O método intersection() retornará um novo conjunto, que contém apenas os itens presentes em ambos os conjuntos. Por outro lado, o método intersection_update() manterá apenas os itens presentes em ambos os conjuntos.
O método symmetric_difference() retornará um novo conjunto, que contém apenas os elementos que NÃO estão presentes em ambos os conjuntos. Por fim,o método symmetric_difference_update() manterá apenas os elementos que NÃO estão presentes em ambos os conjuntos.
Pessoal, para ajuda-los a internalizar o conteúdo, segue uma tabela com os métodos intersection(),intersection_update(), symmetric_difference(), e symmetric_difference_update().

MÉTODO DESCRIÇÃO EXEMPLO

Gera novo conjunto, que contem apenas os ,z = x.mtersection

INTERSECTION_UPDATE(]
SYMMETRIC.DIFFERENCEÍ]

SYMMETRIC_DIFFERENCE_UPDATE(]

itens presentes em ambos os conjuntos

Manterá apenas os itens presentes em . ,

, x.intersection update(y)

ambos os conjuntos.

Novo conjunto, que contém apenas os elementos que NÃO estão presentes em z = x.symmetric_difference(y)ambos os conjuntos

Manterá apenas os elementos que NÃO . z x estão presentes em ambos os conjuntos.
x.symmetric difference update(y)

Abaixo é apresentada a tabela contendo o conjunto de métodos integrados que você pode usar em conjuntos.
MÉTODO DESCRIÇÃO

/ 174

/

ADD[] Adiciona um elemento ao conjunto
CLEARO Remove todos os elementos do conjunto
COPYO Retorna uma cópia do conjunto

DIFFERENCEt] Retorna um conjunto contendo a diferença entre dois ou mais conjuntos

DIFFERENCE_UPDATE[] Remove os itens neste conjunto que também estão incluídos em outro conjunto especificado
DISCARDO Remove o item especificado

INTERSECTIONÍJ Retorna um conjunto, que é a interseção de dois outros conjuntos

INTERSECTION_UPDATE(] Remove os itens neste conjunto que não estão presentes em outros conjuntos especificados
ISDISJOINTO Retorna se dois conjuntos têm uma interseção ou não

ISSUBSETO Retorna se outro conjunto contém este conjunto ou não

ISSUPERSETO Retorna se este conjunto contém outro conjunto ou não

POP[] Remove um elemento do conjunto

REMOVEU Remove o elemento especificado

SYMMETRIC_DIFFERENCE[] Retorna um conjunto com as diferenças simétricas de dois conjuntos

SYMMETRIC_DIFFERENCE_UPDATE[] Insere as diferenças simétricas deste conjunto e de outro
UNIONO Retorna um conjunto contendo a união de conjuntos
UPDATEU Atualize o conjunto com a união deste conjunto e outros

Dicionários Python

Os dicionários são usados para armazenar valores de dados em pares chave:valor. Um dicionário é uma coleção ordenada - a partir do Python 3.7, mutável e que não permite duplicatas.Os dicionários são escritos com colchetes e possuem chaves e valores:
carros = {

"marca": "Toyota",
"modelo": "Corolla Cross",
"ano": 2022

}

Para referenciar um item do dicionário usa-se o nome da chave. Por exemplo, caso você queira referenciar esse magnífico carro, você pode digitar o seguinte comando:print(carros["modelo"]).
Quando dizemos que os dicionários estão ordenados, significa que os itens têm uma ordem definida, e essa ordem não será alterada. Por outro lado, obviamente, não ordenado significa que os itens não têm uma ordem definida, você não pode fazer referência a um item usando um índice.
Os dicionários são mutáveis, o que significa que podemos alterar, adicionar ou remover itens após a criação do dicionário. Ademais, os dicionários não podem ter dois itens com a mesma chave.
MÉTODO DESCRIÇÃO

CLEARO Remove todos os elementos do dicionário

COPYÍJ Retorna uma cópia do dicionário

FROMKEYSÍ) Retorna um dicionário com as chaves e o valor especificados

GETU Retorna o valor da chave especificada

ITEMSU Retorna uma lista contendo uma tupla para cada par de valores-chave

KEYSU Retorna uma lista contendo as chaves do dicionário

POPO Remove o elemento com a chave especificada

POPITEMl) Remove o último par de valores-chave inserido

SETDEFAULTO Retorna o valor da chave especificada. Se a chave não existir: insira a chave, com o valor especificado
UPDATEU Atualiza o dicionário com os pares de valores-chave especificados

VALUESO Retorna uma lista de todos os valores no dicionário

/ 174

/

LISTA E UMA COLEÇÃO ORDENADA E MUTÁVEL. PERMITE MEMBROS DUPLICADOS.

TUPLA E UMA COLEÇÃO ORDENADA E IMUTÁVEL. PERMITE MEMBROS DUPLICADOS.

SET E UMA COLEÇÃO NAO ORDENADA, IMUTÁVEL E NAO INDEXADA. NENHUM MEMBRO
DUPLICADO.

DICIONÁRIO E UMA COLEÇÃO ORDENADA E MUTÁVEL. NENHUM MEMBRO DUPLICADO.

CRITÉRIO LIST TUPLE SET
DICTIONARY

ORDENAÇÃO Ordenada Ordenada Não ordenada
Não ordenada

MODIFICAÇÃO Mutável Imutável
Mutável Mutável

DUPLICATAS Permite duplicatas Permite duplicatas Não permite duplicatas
Não permite duplicatas
INDEXAÇÃO Por inteiro Por inteiro Não indexada Por string
DELIMITADOR Entre colchetes [ ] Entre parênteses () Entre chavesH
Entre chaves

CATEGORIA | TIPO PYTHON
EXEMPLO |

BOOLEANO Booleano bool x = True

Inteiro int x = 10

NUMÉRICO Ponto Flutuante float x = 10.7

Complexo complex x = 345 j

TEXTUAL Texto str x = 'texto'

Lista list x = [4, 8]

Tupla tuple x = (5, 10)

COLEÇÃO/SEQUÊNCIA

x = tuple()

x = {2, 4}

x = set( )

Dicionário dictionary x = {'nome': 'Diego', idade: 31}

(CESPE - PC PB- 2022) Python é uma linguagem procedural que utiliza quatro tipos de dados predefinidos para lidar com coleções: conjuntos, dicionários, listas e tuplas. Arespeito desses tipos de dados, julgue os itens a seguir.

I O conjunto permite o armazenamento de uma tupla, mas não o de uma lista.

II A tupla é idêntica à lista, exceto pela forma mais simples com que sua declaração é realizada.
III A lista é um tipo de dados variável que permite a alteração de seus elementos após a sua criação.
Assinale a opção correta.

a) Apenas o item I está certo.

b) Todos os itens estão certos.

c) Apenas o item II está certo d) Apenas os itens I e III estão certos.
e) Apenas os itens II e III estão certos.

Comentários: Pessoal, vamos começar pelo erro do item II: Uma tupla é uma estrutura bastante similar a uma lista, com uma diferença especial: os elementos inseridos em uma tupla não podem ser alterados, o que não ocorre em uma lista, já que nesta podem ser alterados livremente. Ademais, vejamos o item I: conjunto permite o armazenamento de uma tupla, mas não o de uma lista. Está correto o item I, porque os elementos de um conjunto não são armazenados em uma ordem específica além disso, conjuntos não contém elementos repetidos. Portanto, conjuntos são diferentes de listas. Por fim, o item III está correto,é possível a alteração dos elementos de uma lista. (Gabarito: Letra D).

Condições do Python

Python suporta as condições lógicas usuais da matemática. Essas condições podem ser usadas de várias maneiras, mais comumente em "instruções if" e loops. Uma "instrução if" é escrita usando a palavra-chave if.
a = 33

b = 200

if b > a:

print("B é maior que A")

Vejamos as condições lógicas usuais da matemática que podem ser utilizadas.
Igual a: a == b

Diferentes: a != b
Menor que: a < b

Menor ou igual a: a <= b
Maior que: a > b

Maior ou igual a: a >= b

Pessoal, Python é diferente de outras linguagens como C e Java, que usam colchetes para definir o escopo de um código (função ou classe, por exemplo). Python usa a indentação (espaço em branco no início de uma linha) para definir o escopo no código. Veja que no exemplo anterior, o print após a instrução IF(print("B é maior que A")) possui uma indentação (espaço em branco).Isso faz com que o que possui recuo está dentro da instrução if.
Além da instrução if, há a instrução elif. Elif nada mais é que um else com um if... ou seja, senão se. O Elif é uma maneira de dizer "se as condições anteriores não forem verdadeiras,tente esta condição".
a = 33

b = 33

if a > b:

print("A é maior que B")
if b > a:

print("B é maior que A")
elif a == b:

print("A e B são iguais")

Neste caso, será impresso na tela que "a e b são iguais".

/ 174

/

Pessoal, o if é muito utilizado na prática, além disso cai muito em provas! Além dele, temos o else,que é exatamente o contrário... a instrução if testa se uma condição é verdadeira, já o else, captura o resultado do que não "entrar" na instrução if. Um ótimo exemplo para isso é testar se uma pessoa é maior ou menor de idade. Vejamos um exemplo idade = 18
if idade >= 18:

print('maior de idade')

else:

print('menor de idade')

A palavra-chave else captura qualquer coisa que não seja capturada pelas condições anteriores.

idade = 18

if idade < 12:

print('crianca')
elif idade < 18:

print('adolescente')
elif idade < 60:

print('adulto')

else:

print('idoso')

Além de todas essas formas de criar uma condição, é possível criar uma condição em uma única linha:
if a > b: print("A é maior que B")

O mais incrível ainda é criar um if e else em apenas uma linha! É possível em
Python! Veja o exemplo:
a = 2

b = 330

print("A") if a > b else print("B")

O exemplo acima, irá imprimir na tela B, já que b = 330. Você também pode ter várias instruções else na mesma linha:
a = 330

b = 330

print("A") if a > b else print("=") if a == b else print("B")

/ 174

/

A palavra-chave and é um operador lógico e é usada para combinar instruções condicionais:
a = 200

b = 33

c = 500

if a > b and c > a:

print("Ambas condições são verdadeiras")

Além disso temos a palavra-chave or que é outro um operador lógico usado para combinar instruções condicionais. Ele retorna True se uma das condições for verdadeiras, caso contrário retorna False a = 200
b = 33

c = 500

if a > b or c > a:

print("Uma das condições é verdadeira")

Porfim, a palavra-chave not o inverte o resultado: se o resultado da expressão for
True, o operador retorna false. ®
OPERADOR DESCRIÇÃO
EXEMPLO

Retorna True se todas as condições forem verdadeiras, caso contrário retorna False
Retorna True se uma das condições for verdadeiras, caso contrário retorna False
Inverte o resultado: se o resultado da expressão for True, o operador retorna false x> íand x< 5x> i orx < 5

not(x > i and x < 5)

*

Python While Loops

Com o loop while podemos executar um conjunto de instruções desde que uma condição seja verdadeira. O loop while requer que as variáveis relevantes estejam prontas, no exemplo abaixo precisamos definir uma variável de indexação, i, que definimos como 1.
i = 1

while i < 6:
print(i)

i += 1 # imprime 12345 (um abaixo do outro)

Além disso, podemos parar uma estrutura de repetição utilizando a instrução break. Com a instrução break podemos parar o loop mesmo se a condição while for verdadeira. Por outro lado, a instrução continue para a iteração atual e continuar com a próxima.
i = 1

while i < 6:
print(i)
if i == 3:

break i += 1
No exemplo acima, será impresso na tela i 2 3. E irá parar quando entrar no if i == 3 pois foi inserido um comando break dentro dessa condicional.
i = 0

while i < 6:
i += 1

if i == 3:

continue print(i)
No exemplo acima, serão impressos todos os números da sequência de 1 a 6 exceto o
3. Lembre-se que a instrução continue interrompe a iteração atual e continua com a próxima.Portanto, quando o valor da variável i for 3, vai pular o print e prosseguir o loop.
(FGV - FunSaúde CE- 2021) Observe o código Python V2.7
def F (a, b):

while a != b:

/ 174

/

if a > b:

a = a - b elif b > a:
b -= a return a
Assinale o valor retornado para F (48,36).

a) i b) 12
c) 24

d) 36

e) 48

Comentários: O código consiste em um loop seguido de um condicional. O loop while roda enquanto a variável a tiver um valor diferente de b, assim, resolve-se a condicional. Como 48 é diferente de 36, entramos no condicional, se 48>36 então, a vai receber a - b. a = 46 e b = 36. A vai receber = 12 e retorna esse valor que será impresso. Assim,nosso gabarito é a letra B.
(Gabarito: Letra B).

Loop for em Python

Com toda certeza esse é um dos tópicos mais importantes da aula! Afinal, o que é um loop for? Um loop for é usado para iterar sobre uma sequência (que é uma lista, uma tupla, um dicionário, um conjunto ou uma string). Traduzindo para o português, for é "para", ou seja, a sintaxe é: para uma lista de valores de 1 até 10 (por exemplo), faça isso. Um bom exemplo: para um vetor de 10 variáveis imprima o valor de cada variável. Isso seria traduzido em algo como:
numeros = [1,2,3,4,5,6,7,8,9,10]

for x in numeros:
print(x)

Se você quiser imprimir as letras de seu nome, você pode fazer um loop for para brincar um pouco.Pode fazer isso com qualquer string! Uma string consiste em uma sequencia de caracteres.

umaStringQualquer = "Estratégia Concursos for x in umaStringQualquer:
print(x)

Usando o loop for é possível executar um conjunto de instruções, uma vez para cada item de uma lista, tupla, conjunto etc. É possível usar o comando break e continue no loop for.
Uma das formas mais usadas, e mais cobradas em provas é utilizar o range(). O
range() retorna uma sequência de números, começando do o(zero) (por padrão), incrementando por 1 (por padrão) e termina no número especificado. Ela pode ser utilizada em conjunto com a função for para iterar sobre um bloco de instruções por um número específico de vezes. Vamos ver como funciona:
for x in range(6):

print(x) #Imprimirá 012345

Lembrem-se também que essa função pode ser um pouco mais complexa quando possui todos os seus três parâmetros: start, stop e step. Vejamos um exemplo:
for x in range(2, 20, 3):

print(x) #Imprimirá 2 5 8 11 14 17

Note que o for itera sobre o conjunto de valores que se inicia em 2 (incluso) até
20 (não incluso),
pulando de três em três unidades. Agora vejamos a quantidade de questões sobre loop for

(FGV - TCU - 2022) A execução desse código na IDLE Shell produz, na ordem e exclusivamente, os números:
def xpto(S):

for k in range(0,len(S)):
if k%2 == 0:

yield(S[k]);

S=[l,2,3,4,5,6]

for x in xpto(S[::-1]):
print (x)

a) 6,1

b) 5, 3,1

c) 6, 4, 2

d) 1, 3, 5

e) 2, 4, 6

Comentários: Pessoal, precisamos entender 0 que a função faz. xpto consiste em uma função com um for que percorre S. Caso0 valor k da lista S seja par (2, 4, 6), então ele cria uma lista (S) com os valores pares (2, 4,
6). Veja que 0 retorno da função é exatamente a lista gerada pelo yield(S[k]). Agora vamos para 0 código principal. Após a criação da lista S=[i,2,3,4,5,61, temos forxin xpto(S[::-i]): nesse ponto devemosficar atentos ao -1. O -1 inverte a lista. Enviando para xpto a lista [6,5,4,3,2,11. Assim,quando passar pela função xpto, teremos como resultado apenas os valores pares de
[6,5,4,3,2,11, ou seja, 6,4,2. Portanto 0
gabarito é a letra c. (Gabarito: Letra C).

(FGV - MPE GO- 2022) Assinale a lista de números produzida pela execução, na IDLE
Shell 3.9.9, do código Python a seguir.

forx in range(-i, -10, -1):
print (x)

a) -1-2-3-4-5-6-7-8-9

b) -9 -8 -7-6-5-4 -3-2-1

c) o-1-2-3 -4-5-6-7 -8 -9

d) o -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

e) -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

Comentários: Pessoal, as bancas gostam muito de índices negativos, para dificultar um pouco. No caso da questão, é gerada uma sequência de números negativos iniciando em -1 e parando antes do -10 (ou seja, o for para no-9). O For é incrementado de -1 em -1 formando a sequência -1 -2 -3 -4 -5 -6 -7 -8 -9. (Gabarito: Letra A).
(FGV - PC AM- 2022) Considere o código Python a seguir.
L=[o, 1,1,2,3,5,8,13,21]

for k in range(o,len(l_),2):

print (L[k])

Assinale o resultado exibido pela execução desse código, na IDLE Shell 3.9.9.
a) 1, 2, 5,13

b) 0, 1, 3, 8, 2i, 1, 2, 5,13, 21

c) 1, 3, 8, 21,1, 2, 5,13, 21

d) o, 1, 3, 8, 21

e) 0,1, 3, 8

Comentários: A questão consiste em um for que percorre a lista L e avança de 2 em 2 posições (for k in range(o,len(L),2):). Ele percorre sempre de 2 em 2 posições, portanto, a variável k procurará os valores das posições pares:Posições 0,2,4,6,8. Tenham em mente que 0 valor da posição 0 é 0, da posição 1 é 1, da posição 2 é 1, da posição 3 é 2 e assim por diante, veja:L=[o,i,i,2,3,5,8,13,21]. Se for necessário, desenhe as listas (uma em cima da outra) POSIÇÕES =
[0,1,2,3,4,5,6,7,8,91 LISTA =
[0,1,1,2,3,5,8,13,21].(Gabarito: Letra D).

(FGV- MPE SC- 2022) Analise o código Python a seguir.
s=o for k in range(i6,io, -2):
s -= k print (s)
O valor exibido pela execução desse trecho é:

a) 0

b) -28

c) -30

d) -42

e) -52

Comentários: Pessoal, for k in range(i6,io, -2):gera 16,14 e 12. Nessa sequência, s -=
k vai somar os valores negativos da seguinte forma: -16 -14 e -12 que gera como resultado -42.(Gabarito: Letra D).
Funções do Python

Uma função é um bloco de código que só é executado quando é chamado. Você pode passar dados,conhecidos como parâmetros, para uma função. Essa função pode retornar dados como resultado. Para criar uma função, utiliza-se a palavra-chave def:
def minhafuncao():
print("01á Mundo!")

Para chamar uma função, use o nome da função seguido de parênteses:
minhafuncao()

As informações podem ser passadas para funções como argumentos. Os argumentos são especificados após o nome da função, dentro dos parênteses. Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula. O exemplo a seguirtem uma função com um argumento (nome). Quando a função é chamada, passamos um primeiro nome, que é usado dentro da função para imprimir o nome completo:
def minhafuncao(nome):
print("Prof. " + nome)

minhafuncao("Diego Carvalho")
minhafuncao("Raphael Lacerda")
minhafuncao("Paolla Ramos")

Por padrão, uma função deve ser chamada com o número correto de argumentos. Isso significa que,se sua função espera 2 argumentos, você deve chamar a função com 2 argumentos, nem mais, nem menos. Além disso, se você tentar chamar a função com mais ou menos argumentos,receberá um erro. No caso da função do exemplo, se passar um argumento a menos, receberá o erro:missing 1
required positional argument, por outro lado, se inserir dois argumentos quando era necessário um, receberá o seguinte erro: takes 1 positional argument but 2 were given.
Se você não souber quantos argumentos serão passados para sua função, adicione um
*antes do nome do parâmetro na definição da função. Dessa forma, a função receberá uma tupla de argumentos. Vejamos um exemplo.
def minhafuncao (*professores):

print( professoresfl] + " é um professor de TI do Estratégia")
minhafuncao("Diego Carvalho", "Raphael Lacerda")

No exemplo anterior, será impresso Raphael Lacerda é professor de TI do
Estratégia. A tupla professores possui dois valores: ("Diego Carvalho", "Raphael Lacerda"). A posição o refere-se aDiego Carvalho e a posição 1 refere-se a Raphael Lacerda. Vejamos agora como passar argumentos na função usando chave-valor. Desta forma, a ordem dos argumentos não importa.
def minhafuncao (profl, prof2, prof3):

print( profl + " é um professor de TI do Estratégia")

minhafuncao(profl = "Diego Carvalho", prof2 = "Raphael Lacerda",
prof3 = "Paolla
Ramos")

Se você não souber quantos argumentos de palavra-chave serão passados para sua função,adicione dois asteriscos: ** antes do nome do parâmetro na definição da função. Desta forma a função receberá um dicionário de argumentos.
Outra forma de passar argumentos é enviando uam função. Você pode enviar qualquer tipo de dado de argumento para uma função (string, número, lista, dicionário etc.), e ele será tratado como o mesmo tipo de dado dentro dela. Por exemplo, se você enviar uma lista como argumento,ela ainda será uma lista quando chegar à função:
def minhafuncao(professores):
for x in professores:

print(x)

listadeprofessores("Diego Carvalho", "Raphael Lacerda", "Paolla
Ramos")
minhafuncao(listadeprofessores)

Para permitir que uma função retorne um valor, use a instrução return def funcao(x):return 5 * x print(funcao(3))print(funcao(5))
print(funcao(9))

## imprime 15

## imprime 25

## imprime 45

Python também aceita funções recursivas, o que significa que uma função definida pode chamar a si mesma. A recursão é um conceito matemático e de programação comum. Isso tem a vantagem de significar que você pode percorrer os dados para chegar a um resultado.
O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil escrever uma função que nunca termina, ou uma que usa quantidades excessivas de memória ou poder do
/ 174

/

processador. No entanto, quando escrita corretamente, a recursão pode ser uma abordagem de programação muito eficiente e matematicamente elegante.
OBA, BISCOITO

DA sorte:

O exemplo mais clássico, e para mim, o melhor, é o fatorial em python! É sério galera, é incrível! Ou no mínimo, é assim que você descobre como Python é incrível! Por exemplo, se você atribuir 5 a uma variável "valor", eia uma variável "fatorial", teremos o seguinte código em Python calculando o fatorial.
while (valor > 1):

fatorial = fatorial * valor valor = valor - 1
*

Python Lambda

Uma função lambda é uma pequena função anônima. Ela pode receber qualquer número de argumentos, mas pode ter apenas uma expressão. Vejamos um exemplo de uma função lambda.
x = lambda a : a + 10
print(x(5))

As funções lambda podem receber qualquer número de argumentos. Por exemplo, vejamos como multiplicar um argumento a por argumento b e retornar o resultado:
x = lambda a, b: a * b print(x(5? 6))
O poder do lambda é melhor apresentado quando você os usa uma função anônima dentro de outra função. Digamos que você tenha uma definição de função que recebe um argumento e esse argumento será multiplicado por um número desconhecido:
def minhafuncao(n):
return lambda a: a * n

Usando essa definição de função, é possível para fazer uma função que sempre duplique o número que você envia:
def minhafuncao (n):
return lambda a : a * n dobravalor = minhafuncao (2)print(dobravalor(10)) #imprime 20

,

Matrizes ou Arrays Python

Arrays são usados para armazenar vários valores em uma única variável. O Python não possui suporte integrado para Arrays, mas as Listas do Python podem ser usadas. Para trabalhar com arrays em Python você terá que importar uma biblioteca, como a biblioteca NumPy4.
Um array é uma variável especial, que pode conter mais de um valor por vez.

Se você tiver uma lista de itens (uma lista de nomes de carros, por exemplo),
armazenar os carros em variáveis únicas pode ficar conforme o código a seguir.
cari = "Ford"
car2 = "Volvo"
car3 = "BMW"

No entanto, e se você quiser percorrer os carros e encontrar um específico? E se você não tivesse 3carros, mas 300? A solução é um array! Um Array pode conter muitos valores em um único nome e você pode acessar os valores referindo-se a um número de índice. Assim, é possível acessar um valor da seguinte forma:
carros = ["Ford", "Volvo", "BMW"]
x = carros[0] # x recebe Ford.

Use o método len() para retornar o comprimento de uma matriz (o número de elementos em uma matriz). É possível usar o método append() para adicionar um elemento a uma matriz.Você também pode usar o método pop() para remover um elemento da matriz.
carros = ["Ford", "Volvo", "BMW"]

x = len(carros) #verifica o tamanho do array carros.append("Honda") #adiciona Honda ao fim do array carros.pop(l) #remove 0 carro da posição 1
É possível usar o método remove() para remover um elemento da matriz. A diferença entre o removeO e o pop() é que o primeiro remove apenas a primeira ocorrência do valor especificado.
MÉTODO DESCRIÇÃO

*

APPENDÍJ
CLEARO
COPYU
COUNTIJ
EXTENDI)
INDEX[]
INSERTI)

PÕPÕ
REMOVEI)
REVERSEI)

SORTI)

Adiciona um elemento no final da lista
Remove todos os elementos da lista
Retorna uma cópia da lista

Retorna o número de elementos com o valor especificado

Adicione os elementos de uma lista (ou qualquer iterável) ao final da lista atual
Retorna o índice do primeiro elemento com o valor especificado

Adiciona um elemento na posição especificada
Remova o elemento na posição especificada
Remova o primeiro item com o valor especificado
Inverte a ordem da lista

Ordena a lista

(FCC - PGE AM- 2022) Em um programa escrito em Python, uma série de dados foram inseridos no array cargos, por meio da instrução abaixo.
cargos = [,lAdvogado"/l,Promotor"/ "Procurador", "Juiz", "Desembargador", "Ministro"];

Para colocar estes dados em ordem alfabética decrescente em um novo array chamado cargos_ordenados utiliza-se a instrução:
a) for cargos_ordenados in cargos reverse True;

b) cargos_ordenados = sorted(cargos,reverse=True);

c) while cargos: cargos_ordenados = cargos- -;

d) cargos_ordenados = descending(cargos);

e) cargos_ordenados = ordered(cargos, descending=True);

Comentários: Pessoal, sort() ordena a lista, no caso, a lista "cargos". A opção reverse=True Inverte a ordem da lista. Portanto nosso gabarito é a Letra B. O resultado da execução da letra B é: ['Promotor','Procurador', 'Ministro', 'Juiz', 'Desembargador',
'Advogado']. As demais alternativas geram erros e não existem. (Gabarito: Letra B).

Pessoal, como as bancas estão cobrando Numpy, vamos ver os conceitos básicos sobre essa biblioteca! O que é NumPy? NumPy é uma biblioteca Python usada paratrabalharcom arrays.Além disso, possui funções para trabalhar no domínio da álgebra linear, transformada de Fourier e matrizes.
O NumPy foi criado em 2005 por Travis Oliphant. É um projeto de código aberto e você pode usá-lo livremente. NumPy significa Python Numérico. Em Python temos listas que servem ao propósito de arrays, mas são lentas para processar. O NumPy visa fornecer um objeto array até50X mais rápido que as listas tradicionais do Python.
O objeto array no NumPy é chamado ndarray, ele fornece muitas funções de suporte que facilitam ndarraymuito o trabalho.
Os arrays são usados com muita frequência na ciência de dados, onde a velocidade e os recursos são muito importantes.
x

/ 174

/

Classes/objetos Python

Python é uma linguagem de programação orientada a objetos. Quase tudo em
Python é um objeto, com suas propriedades e métodos. Uma classe é como um construtor de objetos,ou um
"projeto" para criar objetos.

class MinhaClasse:
x = 5

Para entender o significado das classes, temos que entender a função embutidainit(). Todas as classes possuem uma função chamadainit(), que sempre é executada quando a classe está sendo iniciada. Use a funçãoinit() para atribuir valores às propriedades do objeto ou outras operações que são necessárias quando o objeto está sendo criado.
class Person:

def init(self, name, age):
self.name = name self.age = age pl = Person("3ohn", 36)
print(pl.name)
print(pl.age)

A funçãostr() controla o que deve ser retornado quando o objeto de classe é representado como uma string. Se a funçãostr() não for definida, a representação em string do objeto é retornada:
class Person:

def init(self, name, age):
self.name = name self.age = age def str(self):
return f"{self.name}({self.age})"
pl = Person("3ohn", 36)

print(pl)

Objetos também podem conter métodos. Métodos em objetos são funções que pertencem ao objeto.
class Person:

def init(selfj name, age):
self.name = name self.age = age def myfunc(self):
print("Hello my name is " + self.name)

pl = PersonCUohn", 36)
pl.myfunc()

O parâmetro self é uma referência à instância atual da classe e é usado para acessar as variáveis que pertencem à classe. Ele não precisa ser nomeado self, você pode chamá-lo como quiser, mas deve ser o primeiro parâmetro de qualquer função da classe:
(FGV-TJDFT-2022) Analise o código Python 3.9 a seguir.
class Teste:

def self.altura = xaltura self.largura - xlargura def dimensoes(self):
print("altura = " + str(self.altura) + "\n" \ + "largura = " + str(self.largura))
x = Teste(i2, 20)

x.dimensoes()

Para que a execução desse código exiba altura = 12
largura = 20

o trecho tracejado () na segunda linha deve ser substituído por:

a) init(self, xaltura, xlargura):

b) init(xaltura, xlargura):

c) init (xaltura, xlargura):

d) new (self, args[xaltura, xlargura]):

e) new (self, xaltura, xlargura):

Comentários: Pessoal, utiliza-se a funçãoinit() para atribuirvaloresàs propriedades do objeto. Sendo assim ficamos apenas com as opções a e b. Além de init, é necessário usar o self, que é uma referência à instância atual da classe. Portanto, o correto é a letra A. (Gabarito: Letra A).
x

/ 174

/

Herança Python

A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe. A classe pai é a classe que está sendo herdada, também chamada de classe base. A classe filha é a classe que herda de outra classe, também chamada de classe derivada.Qualquer classe pode ser uma classe pai, então a sintaxe é a mesma da criação de qualquer outra classe.
Para criar uma classe que herde a funcionalidade de outra classe, envie a classe pai como parâmetro ao criar a classe filha.
class Student(Person):
pass

Use a palavra-chave pass quando não desejar adicionar outras propriedades ou métodos à classe.
Agora a classe Student têm as mesmas propriedades e métodos que a classe Person. Use a classe
Student para criar um objeto e execute o método printname x = Student("Mike", "Olsen")x.printname()

Até agora criamos uma classe filha que herda as propriedades e métodos de seu pai.
Queremos adicionar a funçãoinit() à classe filha (em vez da palavra- chave pass).
class Student(Person):

def init(self, fname, lname):

Quando você adiciona a funçãoinit(), a classe filha não herdará mais a funçãoinit() do pai. Afunçãoinit() do filho substitui a herança da funçãoinit() do pai. Por outro lado, caso deseje manter a herança da funçãoinit() do pai, adicione uma chamada à funçãoinit() do pai da seguinte forma:
class Student(Person):

def init(self, fname, lname):
Person.init(self, fname, lname)

Python também tem uma função super() que fará com que a classe filha herde todos os métodos e propriedades de seu pai. Ao usar a função super(), você não precisa usar o nome do elemento pai, ele herdará automaticamente os métodos e propriedades de seu pai.
class Student(Person):

def init(self, fname, lname):

super().init(fname., lname)

Iteradores Python

Um iterador é um objeto que contém um número contável de valores.
Utilizando um iterador,
podemos percorrer todos os valores de um objeto iterável (ex: array). Tecnicamente, em
Python,
um iterador é um objeto que implementa o protocolo do iterador, que consiste nos métodos iter() enext().
Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis. Eles são contêineres iteráveis dos quais você pode obter um iterador. Todos esses objetos têm ummétodo iter() que é usado para obter um iterador. Como sabemos, strings consistem em uma contendo uma sequência de caracteres, assim, strings são objetos iteráveis e podem retornar um iterador minhatupla = ("maça", "banana", "cereja")meuiterador = iter(minhatupla)

print(next(meuiterador))
print(next(meuiterador))
print(next(meuiterador))

Também podemos usar um loop for para iterar através de um objeto iterável. O loop for, na verdade, cria um objeto iterador e executa o método next() para cada loop.
minhatupla = ("maça", "banana", "cereja")
for x in minhatupla:

print(x)

Para evitar que a iteração continue para sempre, podemos usar a instrução Stoplteration.

No métodonext(), podemos adicionar uma condição de término para gerar um erro se a iteração for feita um número especificado de vezes:
Escopo do Python

Uma variável só está disponível dentro da região em que foi criada. Isso é chamado de escopo. Uma variável criada dentro de uma função pertence ao escopo local dessa função e só pode ser usada dentro dessa função.
def funcao():
x = 300

print(x)
funcao()

Conforme explicado no exemplo acima, a variável x não está disponível fora da função,
mas está disponível para qualquer função dentro da função. Veja um exemplo em que a variável local pode ser acessada de uma função dentro da função.
def funcao():
x = 300

def funcaointerna():
print(x)

funcaointerna()
funcao()

Vejamos agora como funciona uma variável global! Uma variável criada no corpo principal do código Python é uma variável global e pertence ao escopo global. As variáveis globais estão disponíveis em qualquer escopo, global e local. Uma variável criada fora de uma função é global e pode ser usada por qualquer pessoa.
x = 300 #x é uma variável global!
def myfunc():

print(x)
myfunc()

print(x) #print for a do escopo da funcao!

Se você operar com o mesmo nome de variável dentro e fora de uma função, o Python as tratará como duas variáveis separadas, uma disponível no escopo global (fora da função) e outra disponível no escopo local (dentro da função):
x = 300

def myfunc():
x = 200

print(x) #imprime 200
myfunc()

print(x) #imprime 300

Se você precisar criar uma variável global, mas estiver preso no escopo local, poderá usar a palavra-chave global. A palavra-chave global torna a variável global. Além disso, pode-se usar global se quiser fazer uma alteração em uma variável global dentro de uma função.
def myfunc():
global x x = 300
/ 174

/

Módulos Python

Considere um módulo como sendo o mesmo que uma biblioteca de código. Um arquivo contendo um conjunto de funções que você deseja incluir em seu aplicativo. Para criar um módulo basta salvar o código desejado em um arquivo com a extensão de arquivo .py. Se você criar um código em um arquivo e nomeá-lo como meumodulo.py, você poderá usá-lo invocando "import meumodulo".Além disso, é possível criar um alias ao importar um módulo, usando a palavra-chave as, da seguinte forma.
import meumodulo as mx

O módulo pode conter funções, e variáveis de todos os tipos (arrays, dicionários, objetos etc).

Existem vários módulos integrados no Python, que você pode importar sempre que quiser.
import platform x = platform.system()print(x)

Existe uma função interna para listar todos os nomes de funções (ou nomes de variáveis) em um módulo. A função dir():
import platform x = dir(platform)print(x)

Datas em Python

Uma data em Python não é um tipo de dado próprio, mas podemos importar um módulo chamado datetime para trabalhar com datas como objetos de data.
import datetime x = datetime.datetime.now()
Quando executamos o código do exemplo acima o resultado será a data do momento atual.
A data contém ano, mês, dia, hora, minuto, segundo e microssegundo. O módulo datetime possui muitos métodos para retornar informações sobre o objeto de data.
Para criar uma data, podemos usar a classe datetime() (construtor) do módulo datetime.
A classe datetimeO requertrês parâmetros para criar uma data: ano, mês, dia, conforme pode ser visto no exemplo abaixo. Essa classe também recebe parâmetros para hora e fuso horário (hora,minuto,
segundo, microssegundo, tzone), mas eles são opcionais e têm um valor padrão de o,
(None para fuso horário).
import datetime x = datetime.datetime(2022, 1, 20)
print(x) #imprime 2022-01-20 00:00:00

O objeto datetime tem um método para formatar objetos de data em strings legíveis. O
método é chamado strftime()e usa um parâmetro, format, para especificar o formato da string retornada:
import datetime x = datetime.datetime(2018, 6, 1)print(x.strftime("%B"))

DIRETIVA DESCRIÇÃO
EXEMPLO

%A Dia da semana, versão curta
Wed

%A Dia da semana, versão completa
Wednesday

%W Dia da semana como um número o-6, o é domingo 3

%D Dia do mês 01-31

%B Nome do mês, versão curta
Dec

/ 174

/

December

2018

PM

548513

+ O1OO
CST

%u Número da semana do ano, domingo como o primeiro dia da semana, 00-53
%w Número da semana do ano, segunda-feira como 0 primeiro dia da semana, 00-53
Mon Dec 31 17:41:00

2018

12/31/18

17:41:00

%
2018

Matemática Python

O Python possui um conjunto de funções matemáticas integradas, incluindo um extenso módulo matemático, que permite realizar tarefas matemáticas em números. As funções min()e max()podem ser usadas para encontrar o valor mais baixo ou mais alto em um iterável.

x = min(5? 10, 25)

y = max(5? 10, 25)

print(x) #imprime 5

print(y) #imprime 25

A função abs() retorna o valor absoluto (positivo) do número especificado x = abs(-7.25) # x recebe 7.25 positivo
DIRETIVA DESCRIÇÃO

MATH.ACOSl] Retorna o arco cosseno de um número

MATH.ACOSHO Retorna o cosseno hiperbólico inverso de um número

MATH.ASINÍ] Retorna o arco seno de um número

MATH.ASINHÜ Retorna o seno hiperbólico inverso de um número
MATH.ATANO Retorna o arco tangente de um número em radianos
MATH.ATAN2ÍJ Retorna o arco tangente de y/x em radianos
MATH.ATANHO Retorna a tangente hiperbólica inversa de um número

MATH.CEILO Arredonda um número para o inteiro mais próximo

MATH.COMBÍ]
MATH.COPYSIGNÍ)

MATH.COSO
MATH.COSHÍJ
MATH.DEGREESÍJ

MATH.DISTO

MATH.ERFO
MATH.ERFCO

MATH.EXPMK)

Retorna o número de maneiras de escolher k itens de n itens sem repetição e ordem

Retorna um float que consiste no valor do primeiro parâmetro e o sinal do segundo parâmetro
Retorna o cosseno de um número

Retorna o cosseno hiperbólico de um número
Converte um ângulo de radianos para graus

Retorna a distância euclidiana entre dois pontos (p e q), onde p e q são as coordenadas desse ponto
Retorna a função de erro de um número

Retorna a função de erro complementar de um número
Retorna E elevado à potência de x

Retorna Ex -1

/ 174

/

MATH.FABSO
MATH.FACTORIALÍ)
MATH.FLOORO

706371

MATH.FREXPO
MATH.FSUMO
MATH.GAMMAO
MATH.GCDO

819971

07^314

MATH.ISFINITEd
MATH.ISINFO
MATH.ISNANO
MATH.ISQRTtl
816118

MATH.LGAMMAO

816863

816863

MATH.L0G2O
MATH.PERMO
MATH.POWl)
84^672

MATH.RADIANSÍJ
MATH.REMAINDERÜ

MATH.SINU

^25379

^95371

MATH.TANU
MATH.TANHO
MATH.TRUNCÍJ

Retorna o valor absoluto de um número
Retorna o fatorial de um número

Arredonda um número para baixo para o inteiro mais próximo
Retorna o restante de x/y

Retorna a mantissa e o expoente, de um número especificado

Retorna a soma de todos os itens em qualquer iterável (tuplas, arrays, listas, etc.)
Retorna a função gama em x

Retorna o máximo divisor comum de dois inteiros
Retorna a norma euclidiana

Verifica se dois valores estão próximos ou não
Verifica se um número é finito ou não

Verifica se um número é infinito ou não

Verifica se um valor é NaN (não é um número) ou não

Arredonda um número de raiz quadrada para baixo para o inteiro mais próximo
Retorna o inverso de math.frexpO que é x * (2**i) dos números fornecidos x e i
Retorna o valor de log gama de x

Retorna o logaritmo natural de um número ou o logaritmo do número para a base
Retorna o logaritmo de base 10 de x

Retorna o logaritmo natural de i+x
Retorna o logaritmo de base 2 de x

Retorna 0 número de maneiras de escolher k itens de n itens com ordem e sem repetição
Retorna 0 valor de x elevado a y

Retorna 0 produto de todos os elementos em um iterável
Converte um valor de grau em radianos

Retorna o valor mais próximo que pode tornar 0 numerador completamente divisível pelo denominador
Retorna 0 seno de um número

Retorna 0 seno hiperbólico de um número
Retorna a raiz quadrada de um número
Retorna a tangente de um número

Retorna a tangente hiperbólica de um número
Retorna as partes inteiras truncadas de um número

Python RegEx

Um RegEx, ou Expressão Regular, é uma sequência de caracteres queforma um padrão de pesquisa.RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado.

Python tem um pacote embutido chamado re, que pode ser usado para trabalhar com
Expressões
Regulares. Depois de importar o módulo re, você pode começar a usar expressões regulares. Por exemplo, caso você queira pesquisar uma string para ver se ela começa com "The" e termina com"Spain"

import re txt = "The rain in Spain"
x = re.search("AThe.*Spain$"j txt)

FUNÇÃO DESCRIÇÃO

FINDALL Retorna uma lista contendo todas as correspondências

SEARCH Retorna um objeto Match se houver uma correspondência em qualquer lugar da string

SPLIT Retorna uma lista onde a string foi dividida em cada partida

SUB Substitui uma ou várias correspondências por uma string

CARACTER DESCRIÇÃO
EXEMPLO

Um conjunto de caracteres
"[a-m]"

Sinaliza uma sequência especial (também pode ser usada para escapar de caracteres especiais)
\d"

Qualquer caractere (exceto caractere de nova linha) "he..o"

Começa com
^hello"

Termina com
"planet$"

Zero ou mais ocorrências
"he.*o"

Uma ou mais ocorrências
"he.+o"

Zero ou uma ocorrência
"he.?o"

Exatamente o número especificado de ocorrências "he.{2}o"

Ou
"falls|stays"

Capturare agrupar

/ 174

/

Uma sequência especial é \seguida por um dos caracteres na lista abaixo e tem um significado especial.
CARACTER DESCRIÇÃO
EXEMPLO

Retorna uma correspondência se os caracteres especificados estiverem no início da string
"\AThe"

Retorna uma correspondência em que os caracteres especificados r"\bain"

estão no início ou no final de uma palavra

(o "r" no início está certificando-se de que a string está sendo tratada como uma "string bruta")
r"ain\b"

Retorna uma correspondência onde os caracteres especificados r"\Bain"

estão presentes, mas NÃO no início (ou no final) de uma palavra
(o "r" no início está certificando-se de que a string está sendo tratada como uma "string bruta")
Retorna uma correspondência em que a string contém dígitos
(números de o a 9)

r"ain\B"

"\d"

Retorna uma correspondência onde a string NÃO contém dígitos "\D"

Retorna uma correspondência onde a string contém um caractere de espaço em branco
Retorna uma correspondência em que a string NÃO contém um caractere de espaço em branco
Retorna uma correspondência em que a string contém qualquer caractere de palavra (caracteres de a a Z, dígitos de 0 a 9 e 0caractere sublinhado _)

Retorna uma correspondência em que a string NÃO contém nenhum caractere de palavra
Retorna uma correspondência se os caracteres especificados estiverem no final da string
"\s"

"\S"

"\w"

"\W"

"Spain\Z"

Um conjunto é um conjunto de caracteres dentro de um par de colchetes [] com um significado especial:
CONJUNTO DESCRIÇÃO

[ARN] Retorna uma correspondência em que um dos caracteres especificados (a, r ou n)
está presente
[A-N] Retorna uma correspondência para qualquer caractere minúsculo, em ordem alfabética entre a e n
[AARN] Retorna uma correspondência para qualquer caractere, EXCETO a, r e n

[01231 Retorna uma correspondência onde qualquer um dos dígitos especificados (0,1, 2 ou
3) está presente

[0-91 Retorna uma correspondência para qualquer dígito entre 0 e 9

[0-5H0-9]

Retorna uma correspondência para qualquer número de dois dígitos de 00 a 59

Retorna uma correspondência para qualquer caractere em ordem alfabética entre a e z, minúsculas OU maiúsculas
Em conjuntos, +, */ |, (), $,{} não tem significado especial, então [+] significa:

retornar uma correspondência para qualquer caractere + na string

RESUMO

PALAVRA-CHAVE I DESCRIÇÃO

And é um operador lógico. Os operadores lógicos são usados para combinar instruções

AND
AS
ASSERT

condicionais. O valor de retorno será True somente se ambas as instruções retornarem
Truez caso contrário retornará False.

Usada para criar um alias.

Usada ao depurar o código. Permite testar se uma condição em seu código retorna
Truez caso contrário, o programa gerará um AssertionError. Você pode escrever uma mensagem a ser escrita caso o código retorne false x
/ 174

/

BREAK
CLASS

CONTINUE

DÊF
DEL
ÊLÍF
ELSE

EXCEPT
FALSE

FINALLY

FOR

Usada para quebrar um loop for ou um loop.while

Usada para criar uma classe. Uma classe é como um construtor de objetos.

Usada para encerrar a iteração atual em um loop for (ou loop while) e continua na próxima iteração.
Usada para criar (ou definir) uma função.

Usada para excluir objetos. Em Python tudo é um objeto, então a palavra-chave dei também pode ser usada para deletar variáveis, listas ou partes de uma lista etc.
Usada em instruções condicionais (instruções if) e é abreviação de else if.

com a ramificação "if", tenta as ramificações "elif" e termina com a ramificação "else"
(até ser avaliada comoTrue)

Usada em blocos try...except. Ele define um bloco de código a serexecutado se o bloco try gerar um erro. Você pode definir blocos diferentes para diferentes tipos de erro e blocos para executar se nada der errado
A palavra-chave false é um valor booleano e resultado de uma operação de comparação. A palavra-chave false é igual a o (True é igual a 1).
Usada em blocos try...except. Ele define um bloco de código para ser executado quando o bloco try...except...else for final. O bloco finally será executado independentemente de o bloco try gerar um erro ou não. Isso pode ser útil para fechar objetos e limpar recursos.
Um loop for é usado para iterar sobre uma sequência (que é uma lista, uma tupla, um dicionário, um conjunto ou uma string). Permite executar um conjunto de instruções,uma vez para cada item de uma lista, tupla, conjunto etc.

for i in [0,1,2]:

print(i)

FROM
GLOBAL

IF

IMPORT

IN

is

LAMBDA
NONE

NONLOCAL

Usada para importar apenas uma seção especificada de um módulo.

Usada para criar variáveis globais em um escopo não global, por exemplo, dentro de uma função.
Usada para criar instruções condicionais (instruções if) e permite que você execute um bloco de código somente se uma condição for True. Use a palavra-chave else para executar o código se a condição for False
Usada para importar módulos.

Retorna Verdadeiro se uma sequência com 0 valor especificado estiver presente no objeto. Exemplo: x in y
Retorna Verdadeiro se ambas as variáveis forem o mesmo objeto. Exemplo: x is y

Uma função lambda é uma pequena função anônima. Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.
O objeto Python None, denota falta de valor. Este objeto não tem métodos. É usado para definir um valor nulo ou nenhum valor.
Usada para trabalhar com variáveis dentro de funções aninhadas, onde a variável não deve pertencer à função interna. Use a palavra-chave nonlocal para declarar que a variável não é local.
RAISE
RETURN

TRUE

É um operador lógico. 0 valor de retorno será True se a(s) instrução(ões) não forem
True, caso contrário retornará False.

É um operador lógico Os operadores lógicos são usados para combinar instruções condicionais. O valor de retorno será True se uma das instruções retornar True, caso contrário retornará False.
Usada como um espaço reservado para código futuro. Quando a instrução pass é executada, nada acontece, mas você evita obter um erro quando o código vazio não é permitido. Código vazio não é permitido em loops, definições de função, definições de classe ou em instruções if.
Usada para gerar uma exceção. Você pode definirquetipo de erro gerare otexto a ser impresso para o usuário.
Sai de uma função e retornar um valor.

Valor booleano e resultado de uma operação de comparação. A palavra-chave True é igual a 1 ( False é igual a o).
Usada em blocos try...except. Ele define um bloco de teste de código se ele contém algum erro. Você pode definir blocos diferentes para diferentes tipos de erro e blocos para executar se nada der errado.
Com o loop while podemos executar um conjunto de instruções desde que uma condição seja verdadeira. O loop while requer que as variáveis relevantes estejam prontas (veja que é necessário declarar e atribuir o valor da variável j no exemplo abaixo).
j = o while j < 3:
print(j)
j=j + i

Usado para simplificar 0 tratamento de exceções
Para finalizar uma função, retorna um gerador

FÁCIL: LER, APRENDER E COMPREENDER
MULTIPLATAFORMA, IMENSIDÃO DE MÓDULOS DE EXTENSÃO

74728591

INDENTAÇÃO PARA MARCAÇAO DE BLOCOS
GERENCIA AUTOMATICAMENTE 0 USO DE MEMÓRIA

PROGRAMAÇÃO ORIENTADA A OBJETOS
PROGRAMAÇÃO FUNCIONAL

www. estra tegiaconcursos. com. br

TIPO DE DADO DESCRIÇÃO
EXEMPLO

TEXTO str x = "Hello
World"

Int: x = "Hello World"

NUMÉRICOS int, float, complex

SEQUÊNCIA listz tuplaz range

Float: x= 20.5
Complex: x = ij

List: x = ["maçã", "banana", "cereja"]

Tupla: x = ("maçã", "banana", "cereja")
Range: x= range(6)

MAPEAMENTO dict
Dict: x = {"nomw=e": "John", "idade": 36}

Set: x = {"maçã", "banana", "cereja"}

CONJUNTO set,frozenset

Frozenset: x = frozenset({"maçã",
"banana", "cereja"})

BOOLEANO bool x = True

Bytes: x = b"Hello"

BINÁRIO bytes, bytearray, memoryview

Bytearray: x = bytearray(s)
Memoryview: x = memoryview(bytes(s))

NENHUM TIPO NoneType NoneType:
x = None

MÉTODOS PARA MODIFICAR

STRINGS
UPPERl)
A6D

Retorna a string em maiúsculas
Retorna a string em letras minúsculas

DESCRIÇÃO

STRIPO
REPLACEl)

SPLITU

Remove qualquer espaço em branco do início ou do fim
Substitui uma string por outra string. Ex: replace("h", "j")

Retorna uma lista em que o texto entre o separador especificado se torna os itens da lista.
CARACTER DE ESCAPE I_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ DESCRIÇÃO_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

V

Barra invertida
Nova linha

Volta para margem esquerda e em uma nova linha
Tab

Backspace

Caractere de controle ASCII de quebra de página. Ele força a impressora a ejetar a página atual e a continuar imprimindo na parte superior de outra.
Valor octal

Valor hexadecimal

FUNÇÃO DESCRIÇÃO

CAPITALIZEI)
CASEFOLDÜ

B6D

COUNTO
ENCODEl]
ENDSWITHÍ)
EXPANDTABSO

FÍNDõ
FORMATO
FORMAT_MAP[)

INDEXO

ISALNUMO

ISASCIIO
ISDECIMALO
ISDIGITO
ISIDENTIFIERO
ISLOWERO

204013

ISPRINTABLEO

ISSPACEO
ISTITLEO
ISUPPERO

Converte o primeiro caractere em maiúscula
Converte string em minúsculas

Retorna uma string centralizada

Retorna o número de vezes que um valor especificado ocorre em uma string
Retorna uma versão codificada da string

Retorna verdadeiro se a string terminar com o valor especificado
Define o tamanho da guia da string

Pesquisa a string por um valor especificado e retorna a posição de onde foi encontrado
Formata valores especificados em uma string

Formata valores especificados em uma string

Pesquisa a string por um valor especificado e retorna a posição de onde foi encontrado
Retorna True se todos os caracteres da string forem alfanuméricos

Retorna True se todos os caracteres da string estiverem no alfabeto
Retorna True se todos os caracteres da string forem caracteres ASCII
Retorna True se todos os caracteres na string forem decimais
Retorna True se todos os caracteres da string forem dígitos

Retorna True se a string for um identificador

Retorna True se todos os caracteres da string forem minúsculos
Retorna True se todos os caracteres da string forem numéricos
Retorna True se todos os caracteres da string forem imprimíveis

Retorna True se todos os caracteres na string forem espaços em branco
Retorna True se a string seguiras regras de um título

Retorna True se todos os caracteres da string forem maiúsculos

JOINÜ
LJUST(]
LOWER(]
LSTRIPU
MAKETRANSO
PARTITIONÍJ
REPLACEU

RFINDl]
RINDEXtl
RJUSTO
RPARTITIONÍ]

RSPLITU
RSTRIPÍ]

SPLITLINESU
STARTSWITHl)

Converte os elementos de um iterável em uma string
Retorna uma versão justificada à esquerda da string
Converte uma string em letras minúsculas

Retorna uma versão de corte à esquerda da string

Retorna uma tabela de tradução para ser usada nas traduções
Retorna uma tupla onde a string é dividida em três partes

Retorna uma string onde um valor especificado é substituído por um valor especificado
Pesquisa a string por um valor especificado e retorna a última posição de onde foi encontrado
Pesquisa a string por um valor especificado e retorna a última posição de onde foi encontrado
Retorna uma versão justificada à direita da string

Retorna uma tupla onde a string é dividida em três partes
Divide a string no separador especificado e retorna uma lista
Retorna uma versão de corte à direita da string

Divide a string no separador especificado e retorna uma lista
Divide a string nas quebras de linha e retorna uma lista

Retorna verdadeiro se a string começar com o valor especificado

STRIPl] Remove espaços em branco (ou caracteres dentro do parêntese) do início/fim da string

SWAPCASEO Troca de maiúsculas, minúsculas tornam-se maiúsculas e vice-versa

TITLEl) Converte o primeiro caractere de cada palavra para maiúscula

TRANSLATEO Retorna uma string traduzida

UPPER[] Converte uma string em maiúscula

ZFILLO Preenche a string com um número especificado de valores o no início

OPERADOR NOME
EXEMPLO

+ Adição x + y

- Subtração x-y

* Multiplicação x * y

"7 Divisão x/y

Módulo x % y

** Exponenciação x**y

77 Floor Division: arredonda o resultado para o número inteiro mais próximo x//y
FUNÇÃO DESCRIÇÃO
IGUALA

x = 5

x = x + 3
x = x - 3
x = x * 3
x = x/3

x = x % 3
x = x // 3
x=x**3

x = x & 3
x = x | 3

X = XA3

x = x » 3
x = x « 3

FUNÇÃO DESCRIÇÃO
IGUALA

Igual x==y

Diferente x != y

Maiorque x > y

Menorque x < y

Maior ou igual a x >= y

Menorou igual a x <= y

OPERADOR | DESCRIÇÃO |
EXEMPLO

AND Retorna True se ambas as declarações forem verdadeiras x < 5 and x < io

OR Retorna True se uma das declarações for verdadeira x < 5 orx < 4

NOT Inverte o resultado, retorna False se o resultado for verdadeiro not(x < 5 and x <
io)

OPERADOR DESCRIÇÃO |
EXEMPLO

IS Retorna True se ambas as variáveis forem o mesmo objeto x is y

IS NOT Retorna True se ambas as variáveis não forem o mesmo objeto x is not y

Retorna True se uma sequência com o valor especificado presente no objeto x in y
Retorna True se uma sequência com o valor especificado não estiver presente no objeto x not in y
DESCRIÇÃO

Define cada bit como 1 se ambos os bits forem 1
Define cada bit como 1 se um dos dois bits for 1

Define cada bit como 1 se apenas um dos dois bits for 1
Inverte todos os bits

Desloque para a esquerda empurrando zeros da direita e deixe os bits mais à esquerda fora
Desloque para a direita empurrando cópias do bit mais à esquerda da esquerda e deixe os bits mais à direita fora
MÉTODO DESCRIÇÃO

APPENDtJ
CLEAREJ

COPYtl
COUNTÍ]
EXTENDO
INDEXO
INSERTO

m
REMOVEU
REVERSEO

Adiciona um elemento no final da lista
Remove todos os elementos da lista
Retorna uma cópia da lista

Retorna o número de elementos com o valor especificado

Adiciona os elementos de uma lista (ou qualquer iterável)z ao final da lista atual
Retorna o índice do primeiro elemento com o valor especificado

Adiciona um elemento na posição especificada
Remove o elemento na posição especificada
Remove o primeiro item com o valor especificado
Inverte a ordem da lista

Inverte a ordem da lista

GO

NÃO PODEMOS ALTERAR, ADICIONAR OU REMOVER ITENS
APÓS A CRIAÇÃO DA TUPLA.

MÉTODO DESCRIÇÃO

COUNTÍJ Retorna o número de vezes que um valor especificado ocorre em uma tupla

INDEXO

Procura na tupla um valor especificado e retorna a posição de onde foi encontrado

MÉTODO | DESCRIÇÃO EXEMPLO

Gera novo conjunto, que contem apenas os .

. . z = x.mtersection(y)
itens presentes em ambos os conjuntos

INTERSECTION_UPDATE[]
SYMMETRIC_DIFFERENCE[]

Manterá apenas os itens presentes em . .

. . x.intersection update(y)
ambos os conjuntos.

Novo conjunto, que contém apenas os elementos que NÃO estão presentes em z = x.symmetric_difference(y)ambos os conjuntos

SYMMETRIC.DIFFERENCE.UPDATEO

Manterá apenas os elementos que NÃO
estão presentes em ambos os conjuntos.

x.symmetric difference update(y) ˣ

MÉTODO | DESCRIÇÃO

ADDO Adiciona um elemento ao conjunto

CLEARO
COPYO
DIFFERENCEU

DIFFERENCE_UPDATE(]

Remove todos os elementos do conjunto
Retorna uma cópia do conjunto

Retorna um conjunto contendo a diferença entre dois ou mais conjuntos

Remove os itens neste conjunto que também estão incluídos em outro conjunto especificado
/ 174

/

DISCARDO Remove o item especificado

INTERSECTIONU Retoma um conjunto, que é a interseção de dois outros conjuntos

INTERSECTION_UPDATE[] Remove os itens neste conjunto que não estão presentes em outros conjuntos especificados
ISDISJOINTO Retorna se dois conjuntos têm uma interseção ou não

ISSUBSETU Retorna se outro conjunto contém este conjunto ou não

ISSUPERSETO Retorna se este conjunto contém outro conjunto ou não

POP[] Remove um elemento do conjunto

REMOVEU Remove o elemento especificado

SYMMETRIC.DIFFERENCEÍ] Retorna um conjunto com as diferenças simétricas de dois conjuntos

SYMMETRIC-DIFFERENCEJJPDATEO Insere as diferenças simétricas deste conjunto e de outro

UNIONd Retorna um conjunto contendo a união de conjuntos

UPDATEO Atualize o conjunto com a união deste conjunto e outros

MÉTODO DESCRIÇÃO

CLEARO Remove todos os elementos do dicionário

COPYO Retorna uma cópia do dicionário

FROMKEYSÍJ Retorna um dicionário com as chaves e o valor especificados

GETO Retorna o valor da chave especificada

ITEMSO Retorna uma lista contendo uma tupla para cada par de valores-chave

KEYSU Retorna uma lista contendo as chaves do dicionário

POPO Remove o elemento com a chave especificada

POPITEMO Remove o último par de valores-chave inserido

SETDEFAULTO Retorna o valor da chave especificada. Se a chave não existir: insira a chave, com o valor especificado
UPDATEO Atualiza o dicionário com os pares de valores-chave especificados

VALUESO Retorna uma lista de todos os valores no dicionário

LISTA E UMA COLEÇÃO ORDENADA E MUTÁVEL. PERMITE MEMBROS DUPLICADOS.

TUPLA E UMA COLEÇÃO ORDENADA E IMUTÁVEL. PERMITE MEMBROS DUPLICADOS.
SET E UMA COLEÇÃO NAO ORDENADA, IMUTÁVEL E NAO INDEXADA. NENHUM MEMBRO

DUPLICADO.

DICIONÁRIO E UMA COLEÇÃO ORDENADA E MUTÁVEL. NENHUM MEMBRO DUPLICADO.

CRITÉRIO | LIST TUPLE | SET
DICTIONARY |

ORDENAÇÃO Ordenada Ordenada Não ordenada
Não ordenada

MODIFICAÇÃO Mutável Imutável
Mutável Mutável

DUPLICATAS Permite duplicatas Permite duplicatas Não permite duplicatas
Não permite duplicatas
INDEXAÇÃO Por inteiro Por inteiro Não indexada Por string
DELIMITADOR Entre colchetes [ ] Entre parênteses () Entre chavesH
Entre chaves

CATEGORIA TIPO PYTHON
EXEMPLO

bool int float complex str list tuple set dictionary x = True x = False x = 10
x = -5

x = 10.7

x = -2.8

x = 345 j x = 2-9j x = 'texto'x = "texto"

x = [4, 8]

x = listO

x = (5, 10)

x = tuple()

x = {2, 4}

x = set( )

x = {'nome': 'Diego', idade: 31}

OPERADOR | DESCRIÇÃO
EXEMPLO

AND Retorna True se todas as condições forem verdadeiras, caso x>iandx<s contrário retorna False
OR Retorna True se uma das condições for verdadeiras, caso contrário x > i orx < 5
retorna False

/ 174

/

NOT Inverte o resultado: se o resultado da expressão for True,
operador retorna false o not(x > i and x < 5)
MÉTODO DESCRIÇÃO

APPENDO Adiciona um elemento no final da lista
CLEARO Remove todos os elementos da lista
COPYÍJ Retorna uma cópia da lista

COUNTO Retorna 0 número de elementos com 0 valor especificado

EXTENDÍJ
INDEXO
INSERTO

PÕPÕ
REMOVER
REVERSEl]

Adicione os elementos de uma lista (ou qualquer iterável) ao final da lista atual
Retorna 0 índice do primeiro elemento com o valor especificado

Adiciona um elemento na posição especificada
Remova 0 elemento na posição especificada
Remova 0 primeiro item com o valor especificado
Inverte a ordem da lista

Ordena a lista

DIRETIVA DESCRIÇÃO
EXEMPLO

%A Dia da semana, versão curta
Wed

%A Dia da semana, versão completa
Wednesday

%W Dia da semana como um número 0-6, 0 é domingo 3

%D Dia do mês 01-31

%B Nome do mês, versão curta
Dec

%B Nome do mês, versão completa
December

%M Mês como um número 01-12

%Y Ano, versão curta, sem século

%Y Ano, versão completa
2018

%H Hora 00-23

%l Hora 00-12

%P MANHÃTARDE
PM

%M Minuto 00-59

%S Segundo 00-59

%F Microssegundo 000000-999999
548513

%Z Deslocamento UTC
+ O1OO

%Z Fuso horário
CST

Número do dia do ano 001-366

Número da semana do ano, domingo como 0 primeiro dia semana, 00-53
Número da semana do ano, segunda-feira como 0 primeiro dia semana, 00-53
Versão local de data e hora

Século

Versão local da data
Versão local do tempo
Um personagem

ISO 8601 ano

Dia da semana ISO 8601 (1-7)

Número da semana ISO 8601 (01-53)

Mon Dec 31 17:41:00

2018

12/31/18

17:41:00

%
2018

DIRETIVA DESCRIÇÃO

MATH.ACOSO
MATH.ACOSHO
MATH.ASINO
MATH.ASINHO
MATH.ATANO
MATH.ATAN2Í1
MATH.ATANHO
MATH.CEILO
MATH.COMBO
MATH.COPYSIGNU

MATH.COSl]

84^177

MATH.DEGREESO
MATH.DISTO

MATH.ERFÍJ
MATH.ERFCU

MATH.EXPMKJ

Retorna 0 arco cosseno de um número

Retorna 0 cosseno hiperbólico inverso de um número
Retorna 0 arco seno de um número

Retorna 0 seno hiperbólico inverso de um número
Retorna 0 arco tangente de um número em radianos
Retorna 0 arco tangente de y/x em radianos

Retorna a tangente hiperbólica inversa de um número
Arredonda um número para o inteiro mais próximo

Retorna 0 número de maneiras de escolher k itens de n itens sem repetição e ordem

Retorna um float que consiste no valor do primeiro parâmetro e 0 sinal do segundo parâmetro
Retorna 0 cosseno de um número

Retorna 0 cosseno hiperbólico de um número
Converte um ângulo de radianos para graus

Retorna a distância euclidiana entre dois pontos (p e q), onde p e q são as coordenadas desse ponto
Retorna a função de erro de um número

Retorna a função de erro complementar de um número
Retorna E elevado à potência de x

Retorna Ex -1

MATH.FABSO
MATH.FACTORIALÜ
MATH.FLOORO

706374

816251

MATH.FSUMU
MATH.GAMMAO
MATH.GCDf]

812971

MATH.ISCLOSEÍ)
MATH.ISFINITEO
MATH.ISINFl]
MATH.ISNANÍ]

80^371

816111

MATH.LGAMMAO

816863

816863

MATH.L0G2ÍJ
MATH.PERMU
MATH.POWl)
84^372

MATH.RADIANSO
MATH.REMAINDERU

MATH.SINl]

^25379

^95371

MATH.TANÍJ
MATH.TANHO
MATH.TRUNCÍ]

Retorna o valor absoluto de um número
Retorna o fatorial de um número

Arredonda um número para baixo para o inteiro mais próximo
Retorna o restante de x/y

Retorna a mantissa e o expoente, de um número especificado

Retorna a soma de todos os itens em qualquer iterável (tuplas, arrays, listas, etc.)
Retorna a função gama em x

Retorna o máximo divisor comum de dois inteiros
Retorna a norma euclidiana

Verifica se dois valores estão próximos ou não
Verifica se um número é finito ou não

Verifica se um número é infinito ou não

Verifica se um valor é NaN (não é um número) ou não

Arredonda um número de raiz quadrada para baixo para o inteiro mais próximo
Retorna o inverso de math.frexpO que é x * (2**i) dos números fornecidos x e i
Retorna o valor de log gama de x

Retorna o logaritmo natural de um número ou o logaritmo do número para a base
Retorna o logaritmo de base 10 de x

Retorna o logaritmo natural de i+x
Retorna o logaritmo de base 2 de x

Retorna 0 número de maneiras de escolher k itens de n itens com ordem e sem repetição
Retorna 0 valor de x elevado a y

Retorna 0 produto de todos os elementos em um iterável
Converte um valor de grau em radianos

Retorna o valor mais próximo que pode tornar 0 numerador completamente divisível pelo denominador
Retorna 0 seno de um número

Retorna 0 seno hiperbólico de um número
Retorna a raiz quadrada de um número
Retorna a tangente de um número

Retorna a tangente hiperbólica de um número
Retorna as partes inteiras truncadas de um número

FUNÇÃO DESCRIÇÃO

Retorna uma lista contendo todas as correspondências

Retorna um objeto Match se houver uma correspondência em qualquer lugar da string
Retorna uma lista onde a string foi dividida em cada partida

Substitui uma ou várias correspondências por uma string

DESCRIÇÃO EXEMPLO

Um conjunto de caracteres
"[a-m]"

Sinaliza uma sequência especial (também pode ser usada para escapar de caracteres especiais)
\d"

Qualquer caractere (exceto caractere de nova linha) "he..o"

Começa com
"Ahello"

Termina com
"planet$"

Zero ou mais ocorrências
"he.*o"

Uma ou mais ocorrências
"he.+o"

Zero ou uma ocorrência
"he.?o"

Exatamente o número especificado de ocorrências "he.{2}o"

Ou
"falls|stays"

Capturar e agrupar

CARACTER DESCRIÇÃO
EXEMPLO

Retorna uma correspondência se os caracteres especificados estiverem no início da string
Retorna uma correspondência em que os caracteres especificados estão no início ou no final de uma palavra
(o "r" no início está certificando-se de que a string está sendo tratada como uma "string bruta")
Retorna uma correspondência onde os caracteres especificados estão presentes, mas NÃO no início (ou no final) de uma palavra(o "r" no início está certificando-se de que a string está sendo tratada como uma "string bruta")
Retorna uma correspondência em que a string contém dígitos
(números de o a 9)

"\AThe"

r"\bain"
r"ain\b"

r"\Bain"
r"ain\B"

"\d"

Retorna uma correspondência onde a string NÃO contém dígitos "\D"

Retorna uma correspondência onde a string contém um caractere de espaço em branco
Retorna uma correspondência em que a string NÃO contém um caractere de espaço em branco
"\s"

"\S"

\w Retorna uma correspondência em que a string contém qualquer caractere de palavra (caracteres de a a Z, dígitos de o a 9 e o caractere sublinhado _)
\w Retorna uma correspondência em que a string NÃO contém nenhum caractere de palavra
\z Retorna uma correspondência se os caracteres especificados estiverem no final da string
V

yw"
"SpainU"

CONJUNTO DESCRIÇÃO

[ARN] Retorna uma correspondência em que um dos caracteres especificados (a, r ou n)
está presente
[A-Nl Retorna uma correspondência para qualquer caractere minúsculo, em ordem alfabética entre a e n
[AARN] Retorna uma correspondência para qualquer caractere, EXCETO a, r e n

[01231 Retorna uma correspondência onde qualquer um dos dígitos especificados (0,1, 2
ou
3) está presente

[0-91 Retorna uma correspondência para qualquer dígito entre 0 e 9

[0-5H0-91 Retorna uma correspondência para qualquer número de dois dígitos de 00 a 59

[A-ZA-ZJ Retorna uma correspondência para qualquer caractere em ordem alfabética entre a e z, minúsculas OU maiúsculas
[+1 Em conjuntos, +, *, ., |, (), $,{} não tem significado especial,
então [+] significa:
retornar uma correspondência para qualquer caractere + na string

Automação de Scripts

Automatizar tarefas básicas do dia a dia é fundamental para aumentar a produtividade e valorizar o tempo. Podemos automatizar uma série de tarefas com a Linguagem Python.Desde a automação de tarefas na interface gráfica do Windows, MacOS ou Linux, passando pela automação da extração de dados via web scraping, extração de dados de arquivos pdf, testes de software, até automação de planilhas do Excel, há pacotes Python que ajudam nas tarefas de automação para facilitar o seu trabalho no dia a dia. Vejamos algumas ferramentas para Automação.
PyAutoGUI

PyAutoGUI permite que seus scripts Python controlem o mouse e o teclado para automatizar as interações com outros aplicativos. A API foi projetada para ser simples. O PyAutoGUIfunciona no
Windows, macOS e Linux e é executado no Python 2 e 3.

PyAutoGUI tem vários recursos:

* Movendo o mouse e clicando nas janelas de outros aplicativos.

* Envio de pressionamentos de tecla para aplicativos (por exemplo, para preencher formulários).

* Faça capturas de tela e forneça uma imagem (por exemplo, de um botão ou caixa de seleção) e encontre-a na tela.
* Localize a janela de um aplicativo e mova, redimensione, maximize,
minimize ou feche
(somente Windows, atualmente).

* Exibircaixas de alerta e mensagem.

pywinauto pywinauto é um conjunto de módulos Python para automatizar a GUI do Microsoft Windows.Na sua forma mais simples, permite enviar ações de mouse e teclado para diálogos e controles doWindows.

Selenium Python

O Selenium é uma poderosa aplicação para automação web e permite uma série de explorações nesse universo.Nesse sentido, se faz importante compreender os componentes do Selenium,suas limitações e vantagens, bem como os principais métodos que serão usados.
Saiba mais com o conteúdo a seguir. Falaremos sobre o Selenium Python e mostraremos um tutorial simples de como conseguir a sua primeira automação na web com essa biblioteca.
O Selenium Python é uma biblioteca com diversos métodos que ajudam na automação web.
Em suma, as funções permitem controlar o funcionamento de uma página e a interação com ela de forma automática. O Selenium webdriver é um dos elementos do conjunto selenium que agrega todos os métodos importantes que ainda vamos ver mais adiante.
É interessante também definir o que vem a ser um webdriver. Um webdriver é justamente um app especial que controla o navegador. Existem drivers específicos para cada navegador hoje,com as características necessárias para lidar com cada um.
Dentro do universo do Selenium Python, temos alguns subconceitos relevantes. São eles:
Selenium
IDE, Selenium RC (Remote control), Selenium WebDriver e Selenium GRID.

No Selenium Python temos vários métodos interessantes que podem ser adotados a depender da necessidade. Para clicar em um elemento, o programador pode adotar o click. Um jeito fácil de achar qualquer clicável na página é find_elements_by_xpath(). O método delete_all_cookies apaga os cookies. Há alguns mais simples também, como o maximize_window e o minimize_window,que maximizam e minimizam janelas, respectivamente. Vejamos a seguir uma lista com vários desses métodos e suas finalidades.
MÉTODO FINALIDADE

BACK Volta no histórico para a página anterior

CLOSE Fecha a página atual

EXECUTE_SCRIPT Executa javascript na janela

FORWARD Vai adiante no histórico, para a próxima página

GET_WINDOW_SIZE Pega o tamanho da janela atual

REFRESH Atualiza a página

GET_SCREENSHOT_AS_FILE Salvar um print da tela

Splinter

Splinter é uma estrutura Python que fornece uma interface simples e consistente para automação de aplicativos da web.
Características principais:

* Fácil de aprender: a API foi projetada para ser intuitiva e rápida de aprender.

* Mais rápido para codificar: automatize as interações do navegador de forma rápida e confiável sem lutar contra a ferramenta.
/ 174

/

* Poderoso: Projetado para casos de uso do mundo real, protege contra peculiaridades de automação comuns.
* Flexível: o acesso a ferramentas de nível inferior nunca é oculto. Quebre o
Selênio bruto a qualquer momento.
* Robusto: O suporte está disponível para vários drivers de automação (Selenium,
Django, Flask,
ZopeTestBrowser).

Splinter é usado para escrever scripts de automação do navegador da web.O projeto tem dois objetivos principais:
* Fornecer uma API comum de alto nível sobre as ferramentas de automação de navegador existentes, como o Selenium. A API é uma camada de abstração amigável e projetada para scripts fáceis e eficientes.
* Fornecer funcionalidade integrada para lidar com pontos problemáticos comuns com a automação do navegador.
Scrapy

Uma estrutura de código aberto e colaborativa para extrair os dados que você precisa de sites. De forma rápida, simples e extensível. Ele é rápido e poderoso permitindo ao desenvolvedor escrever as regras para extrair os dados e deixar o Scrapy fazer o resto. Ademais, é facilmente extensívelpor design, é possível conectar novas funcionalidades facilmente sem ter que tocar no núcleo. Por ser escrito em Python, ele roda em Linux, Windows, Mac e BSD
Windmill

Windmill é uma estrutura de teste de interface do usuário da Web AJAX de código aberto. OWindmill implementa testes entre navegadores, gravação e reprodução no navegador e funcionalidade para depuração rápida e precisa; e integração do ambiente deteste.
pytest

O framework pytest facilita a escrita de testes pequenos e legíveis e pode ser dimensionada para dar suporte a testes funcionais complexos para aplicativos e bibliotecas.
De acordo com o livro Teste do Python com pytest, Brian Okken, pytest é inegavelmente a melhor escolha para testar projetos Python. É uma estrutura de teste completa, flexível e extensível. Omodelo de fixture do pytest permite que você compartilhe dados de teste e procedimentos de configuração em várias camadas de testes. A estrutura pytest oferece recursos poderosos,como

/ 174

/

regravação de assert, parametrização, marcadores, plug-ins, execução de teste paralelo e relatórios claros de falha de teste - sem código clichê.
Escreva testes curtos e de fácil manutenção que expressem com elegância o que você está testando. Acelere os tempos de teste distribuindo testes em vários processadores e executando testes em paralelo. Use as instruções assert integradas do Python em vez de funções auxiliares de assert complicadas para tornar seus testes mais legíveis. Mova o código de configuração para fora dos testes e para os acessórios para separar as falhas de configuração das falhas de teste. Teste condições de erro e casos de canto com testes de exceção esperados e use um teste para executar muitos casos de teste com testes parametrizados. Estenda o pytest com plugins, conecte-o a sistemas de integração contínua e use-o em conjunto com testes tox, mock, cobertura e até mesmo unittest existentes.
ReportLab

ReportLab é um framework usado para a criação de documentos PDF baseados em dados complexos e gráficos vetoriais personalizados. É gratuito, de código aberto e escrito em Python.
Report Markup Language é uma linguagem de estilo XML para descrever o layout de documentos.Você define e manipula qualquer aspecto de um documento, incluindo o conteúdo e o estilo,usando tags. Muitas das tags são semelhantes ao HTML.

A saída do documento PDF é gerada a partir do RML usando o módulo python 'rmhpdf. O
RML é usado em conjunto com Preppyo sistema de modelagem do ReportLab. Foi desenvolvido no final de 2000 e está em uso contínuo de produção desde então. É de código aberto (licença BSD).
PDFMiner

PDFMiner é uma ferramenta de extração de texto para documentos PDF.

* Suporta PDF-1.7. (bem, quase)

* Obtém a localização exata do texto, bem como outras informações de layout (fontes, etc.).

* Executa a análise automática de layout.

* Pode converter PDF em outros formatos (HTML/XML).

* Pode extrair um esboço (TOC).

* Pode extrair conteúdo marcado.

* Suporta criptografia básica (RC4 e AES).

* Suporta vários tipos de fonte (Typei, TrueType, Type3 e CID).

* Suporta linguagens CJK e scripts de escrita vertical.

/ 174

/

* Possui um analisador de PDF extensível que pode ser usado para outros fins.

Borb

Trabalhar com PDF pode ser complexo e desafiador na melhor das hipóteses. É por isso que o borb foi criado com a facilidade de uso em mente. Os usuários não precisam teramplo conhecimento dePDF. Economize tempo, dinheiro e trabalhe mais feliz com borb.

OpenPyXL

openpyxl é uma biblioteca Python para ler/gravar arquivos do Excel 2010
xlsx/xlsm/xltx/xltm.
Nasceu da falta de biblioteca existente para ler/escrever nativamente do Python o formato OfficeOpenXML.

PyXLL

Use o Microsoft Excel como um front-end amigável para o seu código Python. Sem VBA,
apenas
Python! Essa é a proposta do PyXLL. Embora seja um software pago, há uma versão trial que pode ser usada sem custo.
XlsxWriter

XlsxWriter é um módulo Python que pode ser usado para escrever texto,
números, fórmulas e hiperlinks para várias planilhas em um arquivo XLSX do Excel 2007+. Ele oferece suporte a recursos como formatação e diversas outras funcionalidades.
Tagui

Tagui é uma API simples e poderosa de RPA para Python que torna a automação robótica de processos divertida! Você pode usá-lo para automatizar rapidamente tarefas repetitivas que consomem tempo em sites, aplicativos de desktop ou linha de comando. Este pacote foi inicialmente desenvolvido na Universidade de Singapura.
Robot Framework

O Robot Framework é um framework de automação genérica e de código aberto. Ele pode ser usado para automação de teste e automação robótica de processos (RPA). É estudado em um dos cursos da Formação Desenvolvedor RPA.
/ 174

/

REFERÊNCIAS

https://d0cs.pyth0n.0rg/pt-br/3/
https://www.w3schools.com/python/

https://www.treinaweb.com.br/blog/principais-estruturas-de-dados-no-python https://pythonhelp.wordpress.com/2o13/o6/18/conjuntos-em-python/https://numpy.org/doc/stable/reference/generated/numpy.std.html https://www.hashtagtreinamentos.com/automacao-web-no-python https://splinter.readthedocs.io/en/latest/why.html https://scrapy.org/https://d0cs.pytest.0rg/en/7.1.x/c0ntents.html https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/https://docs.reportlab.com/rmlfornewbies/

https://borbpdf.com/

https://blog.dsacademy.com.br/15-pacotes-python-para_automacao/

Questões Cespe

QUESTõES CoMENTADAS

í. (CESPE - DPE RO - 2022) Na linguagem Python, são consideradas sequências mutáveis as a) strings b) cadeias c) tuplas d) listas e) ranges
Comentários:

A lista é mutável, o que significa que podemos alterar, adicionar e remover itens em uma lista após ela ter sido criada. Portanto, as listas são consideradas sequências mutáveis.
Gabarito: Letra D

2. (CEBRASPE - PC PB- 2022) Na linguagem Python, o tipo de uma variável em tempo de execução é definido pelo interpretador pelo recurso denominado a) tipagem dinâmica.
b) modo interativo.

c) sintaxe.

d) interpretação bytecode.

e) empacotamento.

Comentários:

Tipagem dinâmica é uma característica de determinadas linguagens de programação,
que não exigem declarações de tipos de dados, pois são capazes de escolher que tipo utilizar dinamicamente para cada variável, podendo alterá-lo durante a compilação ou a execução do programa.
Gabarito: Letra A

3. (CESPE - PC PB- 2022) Python é uma linguagem procedural que utiliza quatro tipos de dados predefinidos para lidar com coleções: conjuntos, dicionários, listas e tuplas. Arespeito desses tipos de dados, julgue os itens a seguir.
I O conjunto permite o armazenamento de uma tupla, mas não o de uma lista.

II A tupla é idêntica à lista, exceto pela forma mais simples com que sua declaração é realizada.

III A lista é um tipo de dados variável que permite a alteração de seus elementos após a sua criação.
Assinale a opção correta.

a) Apenas o item I está certo.

b) Todos os itens estão certos.

c) Apenas o item II está certo d) Apenas os itens I e III estão certos.
e) Apenas os itens II e III estão certos.

Comentários:

Pessoal, vamos começar pelo erro do item II: Uma tupla é uma estrutura bastante similar a uma lista, com uma diferença especial: os elementos inseridos em uma tupla não podem ser alterados,o que não ocorre em uma lista, já que nesta podem ser alterados livremente. Ademais,
vejamos o item I: conjunto permite o armazenamento de uma tupla, mas não o de uma lista. Está correto o item I, porque os elementos de um conjunto não são armazenados em uma ordem específica além disso, conjuntos não contém elementos repetidos. Portanto, conjuntos são diferentes de listas. Por fim, o item III está correto, é possível a alteração dos elementos de uma lista.
Gabarito: Letra D

4. (CEBRASPE-(C0DEVASF-202i) Na linguagem Python, as listas são coleções de qualquertipo de objetos, com exceção das próprias listas, e seus elementos são alteráveis.
Comentários:

Pessoal, lista é uma coleção ordenada e mutável. Permite membros duplicados. Portanto,
o correto seria dizer: Na linguagem Python, as listas são coleções de qualquertipo de objetos,incluindo as próprias listas, e seus elementos são alteráveis
Gabarito: Errada

5. (CEBRASPE - PF- 2021) O código Python a seguir apresenta como resultado "True".

x= bool(-3)

y = bool("True"*x)
z = bool("False")

print (x and y and z)

Comentários:

POLÊMICA! Pessoal, se você rodar esse programa elevai apresentar como resultado True!
Porém a banca teve a coragem de dizer na justificativa de alteração dos gabaritos que "Oresultado que deveria ser True, e não "True"". Enfim, vamos para o código: x,y e z são possuem o valor "True".
/ 174

/

Quando utilizamos a clase bool para conversões temos uma "regra". Essa regra nos diz que quando um valora ser convertido não for uma constante definida para serfalsa, None ou False;não for zero de nenhum tipo; ou termos uma sequência de coleções vazias vamos ter como retorno um valorTrue. Por isso, x, y e z possuem esse valor. E o operador and de três variáveis
True gera como resultado True.
Gabarito: Errada

6. (CEBRASPE - SERPRO- 2021) As tuplas, embora sejam semelhantes às listas, estão limitadas a, no máximo, cinco níveis.
Comentários:

Primeiro lembrete: TUPLAS SÃO IMUTÁVEIS, listas são mutáveis. E diferentemente do que diz a questão não há a limitação de no máximo, cinco níveis nas tuplas.
Gabarito: Errada

7. (CEBRASPE - SERPRO- 2021) Listas são coleções alteráveis de qualquer tipo de objeto —como, por exemplo, outras listas — capazes de gerar um efeito top-down sem limite de níveis.

Comentários:

Perfeito! Perfeito! As listas são MUTÁVEIS, ou ALTERÁVEIS!

Gabarito: Correta

8. (CEBRASPE - PC DF- 2021) Com relação a mineração de dados, aprendizado de máquina e aplicações Python, julgue o item a seguir.
Uma das aplicações de Python é o aprendizado de máquina, que pode ser exemplificado porum programa de computador que aprende com a experiência de detectar imagens de armas e de explosivos em vídeos, tendo seu desempenho medido e melhorado por meio dos erros e de acertos decorrentes da experiência de detecção.
Comentários:

Vejamos o que diz a própria banca: O exemplo apresentado enquadra-se na definição atual de aprendizado de máquina. "O que é aprendizado de máquina? Duas definições de aprendizado de máquina são oferecidas. Arthur Samuel o descreveu como: "o campo de estudo que dá aos computadores a capacidade de aprender sem serem explicitamente programados". Essa é uma definição mais antiga e informal. Na definição mais moderna, "um programa de computador aprende com a experiência E com relação a alguma classe de tarefas T e medida de desempenho P,se seu desempenho nas tarefas em T, conforme medido por P, melhora com a experiência
E. Por exemplo, jogar damas. E = a experiência de jogar muitos jogos de damas T = a tarefa de jogar damas. P = a probabilidade de o programa vencer o próximo jogo.".
/ 174

/

Gabarito: Correta

9. (CEBRASPE - BANESE- 2021) No que se refere ao pacote NumPy do Python, julgue o item subsequente. O código a seguir retorna o valor do desvio padrão amostrai do conjunto de dados
{1,2,2,3,51

import numpy x= numpy.array([i,2,2,3,5])numpy.std(x,ddof=i)

Comentários:

Pessoal, o código apresentado pela questão importa o pacote numpy, cria uma variável x que recebe o array [1, 2, 2, 3, 5]. Por fim, o método std de numpy retorna o desvio padrão amostrai do conjunto dado (numpy.std(x,ddof=i)).
Gabarito: Correta

10.(CEBRASPE - SEED PR- 2021) Em Python, quando mais de um operador aparece em uma expressão, a ordem de avaliação depende das regras de precedência de cada linguagem.Assim,
ao programar em Python, além de observar essas regras, é preciso considerar, ainda, a forma como a linguagem representa seus operadores, conforme demonstrado nos comandos a seguir.
x=7*3**2°/oZ|.
print (x)

Assinale a opção que corresponde à saída que o compilador Python apresentará para os comandos em questão.
a) i b) 3
c) 7

d) 15

e) 15-75

Comentários:

Pessoal, vamos "traduzir" essa expressão. ** Exponenciação; % Módulo.
Temos aqui um
(7*(3**2))%4) Primeiro: x = 7*9%^ resolvemos o 3 elevado ao quadrado. Depois,
x= Ó3o/o4
multiplicamos nove por 7. Por fim, só resta o módulo da divisão. x= 3, já que 4*15 é 60 e deixa resto
3-

Gabarito: Letra B

n.(CEBRASPE - SEED PR- 2021) Na linguagem de programação Python, existem 3
estruturas para armazenar dados indexados. A estrutura cujos valores são imutáveis depois de sua criação é conhecida como a) lista b) operador c) tupla d) classe e) dicionário
Comentários:

Tupla é uma Lista imutável. O que diferencia a Estrutura de Dados Lista da Estrutura de DadosTupla é que a primeira pode ter elementos adicionados a qualquer momento. Vamos relembrar nossa tabela!
CRITÉRIO | LIST TUPLE | SET
DICTIONARY |

ORDENAÇÃO Ordenada Ordenada Não ordenada
Não ordenada

MODIFICAÇÃO Mutável Imutável
Mutável Mutável

DUPLICATAS Permite duplicatas Permite duplicatas Não permite duplicatas
Não permite duplicatas
INDEXAÇÃO Por inteiro Por inteiro Não indexada Por string
DELIMITADOR Entre colchetes [ ] Entre parênteses () Entre chavesH
Entre chaves

Gabarito: Letra C

12. (CEBRASPE - PF- 2018) Considere os seguintes comandos na programação em Python.
a = " Hello, World!"

print(a.stripO)

Esses comandos, quando executados, apresentarão o resultado a seguir.

a[o]=Hello,
a[i]=World!

Comentários:

Pessoal, errada questão! Na verdade, vai apresentar Hello, World!. Strip Remove espaços em branco (ou caracteres dentro do parêntese) do início/fim da string.
Gabarito: Errada

13. (CEBRASPE - PF- 2018) Considere o programa a seguir, na linguagem Python.

/ 174

/

letras == ["P", "F"]
forx in letras l print(x)
A sintaxe do programa está correta e, quando executado, ele apresentará o seguinte resultado.PF

Comentários:

Pessoal, na verdade há três erros na questão. Vamos imediatamente corrigi-los. Na primeira linha o comando deveria ser letras = ["P", "F"] (com apenas um operador = ). Ademais,deveria ser usado o dois pontos no for, e não deve-se usar colchetes para indentação da função for.Portanto, o correto seria:
letras = ["P", "F"]
forx in letras:
print(x)

Gabarito: Errada í^.fCESPE - 2013 - MPOG - Analista de Sistemas) Em Python, o comando int("i") cria um objeto do tipo int, que recebe 1 como parâmetro no seu construtor.
Comentários:

Essa é uma função de casting! Ela converte variáveis do tipo inteiro, ponto flutuante ou string em um inteiro. No caso, ele está recebendo um número como string (por conta das aspas) e convertendo em um inteiro. Esse número serve de parâmetro para o seu construtor (que é um método que cria um objeto, mas vocês não precisam saber disso).
Gabarito: Correta

15. (CESPE - 2013 - MPOG - Analista de Sistemas) Em Python, o comando int("i") cria um objeto do tipo int, que recebe 1 como parâmetro no seu construtor.
Comentários:

Essa é uma função de casting! O que ela faz? Bem, ela converte variáveis do tipo inteiro, ponto flutuante ou string em um inteiro. No caso, ele está recebendo um número como string(por conta das aspas) e convertendo em um inteiro. Esse número serve de parâmetro para o seu construtor(que é um método que cria um objeto, mas vocês não precisam saber disso).

Gabarito: Correta i6.(CESPE - 2011 - ECT - Analista de Sistemas) A linguagem Python e seu interpretador estão disponíveis para as mais diversas plataformas. Para que seja usado em determinado sistema operacional não suportado, é possível gerar o Python a partir do programa fonte utilizando um compilador C. Nesse caso, o código fonte é traduzido para o formato bytecode, que é multiplataforma e pode ser distribuído de forma independente.
Comentários:

Ele realmente é multiplataforma. Além disso, permite que programas sejam compilados para um formato portável chamado de bytecode. Essa característica faz com que programas escritos nessa linguagem com uma biblioteca padrão sejam executadas da mesma forma em diversos sistemas operacionais que possuam um software interpretador de Python.
Gabarito: Correta

17. (CESPE - 2008 - SERPRO - Analista de Sistemas) Python é uma linguagem livre de alto nível,orientada a objetos e de difícil leitura, pois não permite identação de linhas de código.

Comentários:

Ela realmente é de alto nível, orientada a objetos e de fácil leitura. Além disso,
permite indentação de linhas de código.
Gabarito: Errado

18.(CESPE - 2011 - ECT - Analista de Sistemas) A linguagem Python e seu interpretador estão disponíveis para as mais diversas plataformas. Para que seja usado em determinado sistema operacional não suportado, é possível gerar o Python a partir do programa fonte utilizando um compilador C. Nesse caso, o código fonte é traduzido para o formato bytecode, que é multiplataforma e pode ser distribuído de forma independente.
Comentários:

Ele realmente é multiplataforma. Além disso, permite que programas sejam compilados para um formato portável chamado de bytecode. Essa característica faz com que programas escritos nessa linguagem com uma biblioteca padrão sejam executadas da mesma forma em diversos sistemas operacionais que possuam um software interpretador de Python.
Gabarito: Correta ig.(CESPE - 2008 - SERPRO - Analista de Sistemas) Python é uma linguagem livre de alto nível,orientada a objetos e de difícil leitura, pois não permite identação de linhas de código.

Comentários:

Ela realmente é de alto nível, orientada a objetos e de fácil leitura. Além disso,
permite indentação de linhas de código.
Gabarito: Errado

2o.(CESGRANRIO - 2004 - SECAD/TO - Analista de Sistemas) Um programador de
Python recebeu a tarefa de criar uma função chamada calcular que recebe dois parâmetros. Para executar sua atividade, ele deve utilizar a expressão:
a) def calcular (a,b):

b) function calcular (a,b):

c) import calcular (a,b):

d) procedure calcular (a,b):

e) sub calcular (a,b):

Comentários:

Uma função é definida por meio da palavra-chave def.

Gabarito: Letra A

/ 174

/

Questões FGV

2i.(FGV-TCU -2022) Considere o código Python a seguir.

def xpto(S):

for k in range(0,len(S)):
if k%2 == 0:

yield(S[k])j

S-11,2,3,4,5,6]

for x in xpto(S[::-l]):
print (x)

A execução desse código na IDLE Shell produz, na ordem e exclusivamente, os números:

a) 6,i b) 5, 3/ i c) 6, 4, 2
d) i, 3, 5

e) 2, 4, 6

Comentários:

Pessoal, precisamos entender o que a função faz. xpto consiste em uma função com um for que percorre S. Caso o valor k da lista S seja par (2, 4, 6), então ele cria uma lista (S) com os valores pares(2, 4, 6). Veja que o retorno da função é exatamente a lista gerada pelo yield(S[k]). Agora vamos para o código principal. Após a criação da lista S=[I,2,3,4,5,6], temos for x in xpto(S[::-i]): nesse ponto devemos ficar atentos ao -1. O -1 inverte a lista. Enviando para xpto a lista[6,5,4,3,2,1].
Assim, quando passar pela função xpto, teremos como resultado apenas os valores pares de[6,5,4,3,2,1], ou seja, 6,4,2. Portanto o gabarito é a letra c.

Gabarito: Letra C

22. (FGV - PC AM- 2022) Considere o código Python a seguir.

L=[o,i,i,2,3,5,8,i3,2i]

for k in range(o,len(L),2):

print (L[kj)

Assinale o resultado exibido pela execução desse código, na IDLE Shell 3.9.9.
a) 1, 2, 5,13

/ 174

/

b) o, í, 3, 8, 21, í, 2, 5,13, 21

c) 1, 3, 8, 21,1, 2, 5,13, 21

d) o, 1, 3, 8, 21

e) o, 1, 3, 8

Comentários:

A questão consiste em um for que percorre a lista L e avança de 2 em 2 posições
(for k in range(o,len(l_),2):). Ele percorre sempre de 2 em 2 posições, portanto, a variável k procurará os valores das posições pares: Posições o,2,4,6,8. Tenham em mente que o valor da posição0 é o, da posição 1 é 1, da posição 2 é 1, da posição 3 é 2 e assim por diante, veja:L=[o,1,1,2,3,5,8,13,21]. Se for necessário, desenhe as listas (uma em cima da outra) POSIÇÕES =[0,1,2,3,4,5,6,7,8,9] LISTA =
[0,1/1/2,3,5,8,13,21].

Gabarito: Letra D

23. (FGV - SEFAZ AM- 2022) Analise o código a seguir em linguagem de programação Python:

1 def rotina(array):

2 for p in range(@, len(array))!

3 element = array[p]

5 wtiile ip > 0 and array [ip - 1] > element:

6 ãrray(p) = array[p =- 1]

7 p -= 1

9 arrayfpj element

11 return array

13 print ( rotina([9, S, 31, 42, 20, S6] } }

Ao executar esse script em um terminal, será escrito na saída padrão a) [9, 5, 3i, 42, 20, 56]
b) [8, 4, 30, 41,19, 55]

c) [56, 20, 42, 31, 5, 9]

d) [56, 42, 31, 20, 9, 5]

e) [5, 9, 20, 31, 42, 56]

Comentários:

Pessoal, o código da questão basicamente ordena um array. Dessa forma, a saída será o array ordenado: [5, 9, 20, 31, 42, 56].
Gabarito: Letra E

24. ( FGV - MPE GO- 2022) Considere o código Python a seguir.

/ 174

/

defX(n):

if (type(N) != int):
return -1

elif (N < i):

return o elif (N == i):
return 1
else:

return N *X(N-i)
print (X(4))

print (X(o))

print (X(i))

print (X(i.₅))

print (X("A"))

Assinale o que acontece quando esse script é executada na IDLE SheiI 3.9.9.

a) Erro de compilação, "name 'n ' is not defined"

b) Erro de compilação, "name 'N' is not defined"

c) Executa e produz resultados Corretas com quatro linhas.

d) Executa, mas produz erro de execução na quinta chamada da função X.

e) Executa, mas calcula erradamente o fatorial de 4.

Comentários:

Pessoal, vocês lembram que python é uma linguagem case sensitive? O erro neste caso seráNameError: name 'N' is not defined. Porque na definição temos def X(n),
depois usa-se o N
(maiusculo).

Gabarito: Letra B

25. (FGV-MPE GO-2022) Assinale a lista de números produzida pela execução, na IDLE
Shell 3.9.9,
do código Python a seguir.

for x in range(-i, -10, -1):

print (x)

a) -1-2-3-4-5-6-7-8-9

b) -9 -8 -7 -6 -5 -4 -3 -2 -1

c) o-1-2-3 -4-5-6-7 -8-9

d) o -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

e) -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

Comentários:

Pessoal, as bancas gostam muito de índices negativos, para dificultar um pouco. No caso da questão, é gerada uma sequência de números negativos iniciando em -1 e parando antes do -10 (ou seja, o for para no -9). O For é incrementado de -1 em -1 formando a sequência -1 -2 -3 -4 -5 -6 -7-8

-9-

Gabarito: Letra A

26.(FGV-TJDFT-2022) Analise o código Python 3.9 a seguir.

class Teste:

def self.altura = xaltura self.largura = xlargura def dimensoes(self):
print("altura = " + str(self.altura) + "\n" \ + "largura = " + str(self.largura))
x = Teste(i2, 20)

x.dimensoes()

Para que a execução desse código exiba altura = 12
largura = 20

o trecho tracejado na segunda linha deve ser substituído por:

a) init(self, xaltura, xlargura):

b) init(xaltura, xlargura):

c) init (xaltura, xlargura):

d) new (self, args[xaltura, xlargura]):

e) new (self, xaltura, xlargura):

Comentários:

Pessoal, utiliza-se a funçãoinit() para atribuir valores às propriedades do objeto. Sendo assim ficamos apenas com as opções a e b. Além de init, é necessário usar o self, que é uma referência à instância atual da classe. Portanto, o gabarito é a letra A.
Gabarito: Letra A

27.(FGV-MPE SC-2022) Analise o código Python a seguir.
xi = {"A", "B", "C"}

X2 = ["AA", "BB", "CC"]

xi.add("B")

x2.append("BB")
X2.append(xi)
print (x2)

Dado que os elementos de xi podem ser exibidos em ordem aleatória, a linha que possivelmente é produzida pelo comando print na execução do código acima é:
/ 174

/

a) ['AA', 'BB', 'CC, 'BB', {'C, 'A', 'B'}]

b) ['AA', 'BB', 'CC, 'BB', 'C, 'A', 'B', 'B']

c) ['AA', 'BB', 'CC, 'BB', 'C, 'A', 'B']

d) ['AA', 'BB', 'CC, ['BB'], {'B'}]

e) {'AA','BB', 'CC,'BB','C, 'A', 'B'}

Comentários:

Pessoal, primeiramente devemos desconsiderar xi já que o comando da questão diz que os elementos de xi podem ser exibidos em ordem aleatória. Vejamos então a ordem de X2.Inicialmente temos um ["AA", "BB", "CC"] que consiste no X2 original. Após, teremos BB
(devido ao
X2.append ("BB")). Portanto ficamos com 'AA', 'BB', 'CC, 'BB'. Dessa forma ficamos entre as opções a,b, cee. Porém, depois do X2 há um xi (x2.append(xi)). Dessa forma, podemos ter um["A", "B","C"] em uma sequência aleatória - como diz o comando da questão. A única opção que possui um
{"A", "B", "C"} em sequência aleatória é a letra A.

Gabarito: Letra A

28.(FGV-MPE SC-2022) Analise o código Python a seguir.
s=o for k in range(i6,io, -2):
s-=k print (s)
O valor exibido pela execução desse trecho é:

a) o b) -28
c) -30

d) -42

e) -52

Comentários:

Pessoal, for k in range(i6,io, -2):gera 16,14 e 12. Nessa sequência, s -= k vai somar os valores negativos da seguinte forma: -16 -14 e -12 que gera como resultado -42, nosso gabarito.
Gabarito: Letra D

2g.(FGV-MPE SC-2022) Analise o código Python a seguir,
x = o y - 20
try:

print (y/x)
except:
print("Deu erro!")

else:

print("Ok")
finally:

print ("The end")

A saída produzida pela execução desse trecho é:

a) a) None
The end b) Deu erro!
The end c) Deu erro!
Ok d) OkThe end e) NoneOk

The end

Comentários:

Pessoal, vamos relembrar os conceitos de if, else, finally. finally é usada em blocos try...except. Ele define um bloco de código para ser executado quando o bloco try...except...else for final. O bloco finally será executado independentemente de o bloco try gerar um erro ou não. O foco é esse!Finally será executado independentemente de o bloco try gerar um erro ou não.
Portanto, sabemos que vai imprimir o print "The end", já que, vai entrar no finally. Além disso, há um erro, de divisão por zero (ZeroDivisionError: division by zero), dessa forma, também irá imprimir "Deu erro!". Oresultado será Deu erro! The end.

Gabarito: Letra B

3O.(FGV-MPE SC-2022) Analise o código Python a seguir.

def xpto(L):

return (L[::-i])

A expressão xpto([i,2,3]) retorna:

a) []

b) [i]

c) [3]

d) [i, 2, 3]

e) [3, 2,1]

Comentários:

Pessoal, veja como as bancas gostam de inverter listas! Novamente temos L[::-i] que consiste no comando que inverte a lista passada. Dessa forma, sabemos que o resultado será [3, 2,1].
Gabarito: Letra E

31. (FGV-MPE SC-2022) Analise o código Python a seguir.

class xptoClass:
def iter(self):
self.a = [0]
return self def next(self):self.a.append( \

self.a[-l] \

+ self.a[-2] if len(self.a) > 1 else 1)
return self.a xpto = xptoClass()xptolter = iter(xpto)

for k in range(lj6):

print(next(xptolter))

No resultado produzido pela execução do código acima, a quinta linha contém exatamente:
a) [0,1,1, 2, 2, 3]

b) [o, 1,1, 2, 3, 5]

c) [0,1, 2, 3, 4, 5]

d) [o, 1, 3, 5, 7, 9]

e) [1, 2, 3, 4, 5, 6]

Comentários:

Pessoal, essa questão apresenta a sequência de Fibonacci. Na quinta linha temos o resultado [o, 1,1, 2, 3, 5]. As iterações anteriores são: [o, 1]; [o, 1,1]; [o, 1,1, 2]; [o, 1,1, 2, 3]; [o, 1,1,
2, 3, 5].

Gabarito: Letra B

32. (FGV - IMBEL- 2021) Analise o código Python a seguir.

/ 174

/

x= [1,23,4,5]

print (x[::-i])

Assinale a opção que indica a saída produzida pela execução desse código.

a) [1,2,3,4,51

b) i c) [5,1]
d) 5

e) [5,4,3,2,1]

Comentários:

Pessoal, novamente cobrança da inversão de lista. x[::-i] retorna o inverso da lista passada.Importante, no caso da questão a lista é denominada x, mas pode ter qualquer nome.
As bancas amam! Resposta: e) [5,4,3,2,11.
Gabarito: Letra E

33. (FGV- IMBEL - 2021) Analise o código Python a seguir.

x= [1,23,4,5]

print (x[-il)

Assinale a opção que indica a saída produzida pela execução desse código.

a) [1,23,4,5]

b) 1

c) [5,1]

d) 5

e) [5,4,3,2,1]

Comentários:

Pessoal, (x[-ij) pega o valor da posição 1 do fim da lista para o início. E nesse caso a posição -1 é o valor 5. Portanto, nosso gabarito é a letra D.
Gabarito: Letra D

34.(FGV -TCE-AM- 2021) Considere o código Python, versão 2.7.1, na qual o comando print não requer parênteses.
def teste(n):

for k in range(lj n+1):
yield(k)

for x in teste(10):
print x

/ 174

/

A execução desse código:

a) não tem efeito, pois nenhum comando print é acionado;

b) provoca a exibição do número 10 na saída;

c) provoca a exibição dos números de 1 até 10 na saída;

d) provoca um erro de compilação;

e) provoca um erro de execução

Comentários:

Questão um pouco polêmica, porém a FGV claramente diz em seu enunciado: versão 2.7.1,
na qual o comando print não requer parênteses. Ok! Já que ela disse, vamos considerar que,neste caso, o comando print não requer parênteses! Porque na Versão 2.7.1, de fato, os códigosPython não precisam dos parênteses para o print. Já, na Versão 3 precisa dos parênteses!Desconsiderando isso,
o for da função teste gera uma lista sequencial (1, n+i), e o segundo for apresentar a chamada da função teste com 10 elementos, portanto, a execução desse código provoca a exibição dos números de 1 até 10 na saída.
Gabarito: Letra C

35. (FGV-TJ RO-2021) Analise o código Python 2.7 a seguir.

def xpto (nl, n2):

while nl != n2:

if (nl < n2):

n2 = n2 - nl else:
return nl print xpto(50j5)
nl = nl - n2

O valor exibido pelo comando print é:

a) o b) 1
c) 5

d) 10

e) 50

Comentários:

/ 174

/

Pessoal, o while irá executar até que m != n2, ou seja, m diferente de n2. Dessa forma, ele vai realizar as seguintes operações: 50-5 =45, 45-5=40, 40 -5 - 35 ... até chegar a 5que é o valor de retorno. Portanto, gabarito letra c.
Gabarito: Letra C

36.(FGV- BANESTES-2021) Considere o código Python 2.7 a seguir:
def ABC(L, n):

while True:

if len(L) >= n:

return L
else:

L.append(len(L) ** 2)
print ABC([2o],Io)

O resultado da execução desse código é:

a) [1, 4, 9,16, 25, 36, 49, 64]

b) [1, 4, 9,16, 25, 36, 49, 64, 81]

c) [20,1, 4, 9,16, 25, 36, 49, 64]

d) [20,1, 4, 9,16, 25, 36, 49, 64, 81]

e) [20, 4, 9,16, 25, 36, 49, 64, 81]

Comentários:

Pessoal, é necessário saber que a função principal do código consiste em inserir um elemento no final de uma lista de 10 elementos, perceba: if len(L) >= n aqui, podemos observarque se o tamanho da lista for maior ou igual a n (que vale 10) vai encerrar o Loop e retornar L (a lista). Daí sabemos que a lista terá dez números, então desconsideramos as alternativas com mais ou menos que dez elementos. Nisso, fica apenas a letra D. Mas vamos confirmar nosso gabarito. Oprimeiro valor é 20
passado no print (ABC([2o],Io)), os demais serão 1,4,9,16,25,36,49,64,81.

Gabarito: Letra D

37. (FGV - FunSaúde CE- 2021) Observe o código Python V2.7.
def F (a, b):

1 1 1

/ 174

/

while a != b:
if a > b:

a = a - b elif b > a:
b -= a return a
Assinale o valor retornado para F (48,36).

a) i b) 12
c) 24

d) 36

e) 48

Comentários:

O código consiste em um loop seguido de um condicional. O loop while roda enquanto a variável a tiver um valor diferente de b, assim, resolve-se a condicional. Como 48 é diferente de 36, entramos no condicional, se 48>36 então, a vai receber a - b. a = 46 e b = 36. A vai receber = 12 e retorna esse valor que será impresso. Assim, nosso gabarito é a letra b.
Gabarito: Letra B

38.(FGV - BANESTES-2021) Considere o código Python a seguir.

def F(a, b, c):

for k in range(a,b):

print k**c

Dado que uma execução da função F exibiu os números
16, 9, 4,1, o, 1,

é Correta afirmar que os valores dos parâmetros a, b, c empregados foram, respectivamente:

a) -4,1, 2;

b) -4, 2, 2;

c) -4, 0, 4;

d) 4, -1,1;

e) 4, 2, 2.

Comentários:

Pessoal, nessa questão precisamos saber qual intervalo de valores gera a sequência 16,
9, 4,1, o, 1.
Sabendo que a função consiste em três valores: a, b e c que em que um valor k é elevado a c. Para gerar 16, 9, 4 precisamos de valores elevado ao quadrado, concordam? 42, 32 e 22...Portanto b = 2.
Daí eliminamos quase todas as alternativas exceto b e e. Há um erro sutil na letra
E. O start (4),
primeiro valor, é maior que o stop (2). Por isso, nosso gabarito é a letra B.

Gabarito: Letra B

3g.(FGV- BANESTES-2021) Considere o código Python 2.7 a seguir.

L=[6,5,4,3,2,1]

forkin range(-3,3):

print L[k]

A execução desse código exibe os números:

a) 111654;

b) 123456;

c) 3 2 16 5 4;

d) 6 5 4 3 2 1;

e) 654654.

Comentários:

Pessoal, o for pega os 3 valores - do fim para o início (pega 3,2,1) e depois os três primeiros (pega6,5,4). Nosso gabarito 0321654.

Gabarito: Letra C

4O.(FGV- IMBEL- 2021) Analise o script Python 3.8 exibido a seguir.

L=["A","E","I","O","U"]

for k in range(-i, -5, -1):

print (L[k+i])

Assinale a saída produzida pela execução desse código.

a) AEIOU

b) A E I U

c) A U O I

d) U A E I

e) U O I E A

Comentários:

Mais uma questão com valores negativos! Vejamos o que ela faz! range(-i, -5, -1). Na verdade, o print pega os índices, nessa sequência: -1 + 1 = o; -2 +1 = -1; -3 + 1 = -2; -4 + 1 = -3. Então vai pegar:L[o] = A, L[-i] = U, L[-2] = O, L[-3] = I. Lembrando que os valores negativos iniciam do fim da lista!
Gabarito: Letra C

4i.(FGV-IMBEL-2O2i) Analise o script Python 3.8 exibido a seguir.

for k in range(o,len(L)):

print (L[4-kj)

Assinale a opção que indica a saída produzida pela execução desse código.

a) AEIOU

b) A E I O

c) E I O U

d) U O I E

e) U O I E A

Comentários:

Pessoal, vamos ver quais valores o print está pegando:

L[4-o] = L[4] = U

L[4-I] = L[₃] = O

L[4-2]= L[2]=I

L[4-3l = L[i] = E
L[4-4] = L[o] = A.

Gabarito: Letra E

42.(FGV - DPE RJ- 2019) Analise o código Python 2.7 a seguir.

frutas = ["banana","laranja","manga","uva"]
for k in range(-1,-4,-2):

print frutas [k]

O conjunto de palavras exibidas pela execução desse código, na ordem, é:

a) banana;

b) laranja, manga;

c) uva, laranja;

d) banana, laranja, manga;

/ 174

/

e) banana, laranja, manga;

Comentários:

Inicialmente você deve observar que seu array terá apenas dois elementos, porque a função range está pulando de -2 em -2 elementos - e há 4 elementos no array. O primeiro elemento é o -1, ou seja, uva. O segundo e ultimo será o -3, laranja. Gabarito letra C.
Gabarito: Letra C

43.(FGV- MPE AL-2018) Analise o código Python 2.7 a seguir.

Li=[]
L2=[I,2,3,4]

for k in range(3, -4,-1):

Li.append(L2[k])
forx in L:

print x

Esse programa causa a) erro de sintaxe.
b) erro de execução.

c)a exibição dos valores 4,3,2,1,43,2 nessa ordem.

d) a exibição do valor 4, somente.

e) a exibição dos valores 43,2,1 nessa ordem.

Comentários:

Pessoal, ocorrerá um erro de execução, porque a variável L não foi definida (for x in L), veja:NameError: name ' L' is not defined. Se fosse inserido Li ou L2 no local que foi inserido L, executaria perfeitamente.
Gabarito: Letra B

44-(FGV - 2015 - CM/Caruaru - Analista Legislativo - Informática) Analise o código
Python a seguir.
Li=[io,20,30]
L244030]

Li.append(L2)

print Li

Assinale a opção que descreve corretamente o que acontece quando esse programa é executado no Python 2.7:
a) Produz uma mensagem de erro, porque tenta executar uma operação inválida.

b) Exibe "[io, 20, 30, [40, 50]]".

c) Exibe "[10, 20, 30, 40, 50]".

d) Exibe "[10, 20, 30], [40, 50]".

e) Exibe

Comentários:

O comando append inclui o valor da variável L2 na posição final do vetor Li. Como o conteúdo da variável l_2 é uma lista de tamanho 2 [40,50], ele que será incluído na 4a posição de Li. Professor,porque a resposta não é letra C? Muito bem observado, padawan! O método append inclui a lista l_2como se fosse só um elemento, isto é, a lista final tem 4 elementos ao invés de 5,
pois L2 é tratado como se fosse uma coisa só!
Gabarito: Letra B

45.(FGV - 2015 -TJ/BA - Analista Judiciário) Analise o trecho de programa Python, na versão 2.7,apresentado a seguir.

L=[I,2,3,4,5,6,7,8]

print L[::-i]

Ao ser executado, o resultado exibido é:

a) [1, 2, 3, 4, 5, 6, 7, 8]

b) [8]

c) []

d) [8, 7, 6, 5, 4, 3, 2,1]

e) [1]

Comentários:

O operador de acesso a itens em coleções (listas, sets, tuplas) usam três argumentos:

L[Start:Stop:Step]

Start - primeira posição a ser acessada:

Pode ser: (1) valor positivo - posição inicial de acesso (por exemplo, o é a primeira, 1 é a segunda);
(2) valor negativo - posição a partir do final do array (por exemplo, -1 é a última posição, -2 é a penúltima); (3) não fornecido - primeira posição do array (posição 0).
Stop - última posição a ser acessada:

Pode ser: (1) valor positivo - posição de acesso (por exemplo, o é a primeira, 1 é a segunda); (2)
valor negativo - posição a partir do final do array (por exemplo, -íéa última posição, -2é a penúltima);

(3) não fornecido - última posição do array (posição -1).

Step - valor do incremento no acesso:

Pode ser: (1) número positivo - ordem direta de incremento em incremento; (2) número negativo -ordem inversa de incremento em incremento; (3) não fornecido - ordem de 1 em 1.
Quando só step é fornecido e ele é negativo, ele acessa a coleção de forma invertida a partir do último elemento.
Dessa forma, o acesso L[::-i] acessará da primeira até a última posição do array em ordem inversa,ou seja, [8, 7, 6, 5, 4, 3, 2,1].

Gabarito: Letra D

46.(FGV - 2014 - MPE/AL) Analise o código Python 2.7 a seguir.

L = [10,12,14,16]

for k in range(4, -5, -1):

print L[k]

Esse programa causa:

a) erro de sintaxe.

b) erro de execução.

c) a exibição de 4 valores, 16,14,12,10, nessa ordem.

d) a exibição de 8 valores, 16,14,12,10,16,14,12,10, nessa ordem.

e) a exibição do valor 16, somente.

Comentários:

A questão é fácil de responder porque ela possui erro de sintaxe! A sintaxe exige que o bloco for tenha um corpo, e o corpo precisa seguir o ":" ou estar dentro de um bloco indentado abaixo do"for". Perceba que não acontece nenhum dos dois casos na questão: não existe nada depois do nem existe comando indentado abaixo do "for". E mesmo que estivesse corretamente indentado,
ainda haveria um erro de execução porque o range(4, -5, -1) percorre de 4 a -4 em passos de -1 e não teria como imprimir L[4] porque esse valor sequer existe, L só vai de 0 a 3.
Gabarito: Letra A

/ 174

/

Questões FCC

47.(FCC- PGE AM-2O22)Em um programa escrito em Python, uma série de dados foram inseridos no array cargos, por meio da instrução abaixo.
cargos - ["Advogado","Promotor", "Procurador", "Juiz", "Desembargador", "Ministro"];

Para colocar estes dados em ordem alfabética decrescente em um novo array chamado cargos_ordenados utiliza-se a instrução:
a) for cargos_ordenados in cargos reverse True;

b) cargos_ordenados = sorted(cargos,reverse=True);

c) while cargos: cargos_ordenados = cargos- -;

d) cargos_ordenados = descending(cargos);

e) cargos_ordenados = ordered(cargos, descending=True);

Comentários:

Pessoal, sort() ordena a lista, no caso, a lista "cargos". A opção reverse=True
Inverte a ordem da lista. Portanto nosso gabarito é a Letra B. O resultado da execução da letra B é:['Promotor',
'Procurador', 'Ministro', 'Juiz', 'Desembargador', 'Advogado']. As demais alternativas geram erros e não existem.
Gabarito: Letra B

48.(FCC - TRF 4 - 2019) Considerando que em um programa Python em condições ideais há um array criado pelo comando nomes - ["Maria", "Pedro", "João"], para exibir os valores contidos nesse array utiliza-se a) for x in nomes: out.print(x)
b) while x in nomes: print(x)

c) foreach x in nomes: print(x)

d) foreach x in nomes: system.println(x)

e) for x in nomes: print(x)

Comentários:

Pessoal, fizemos vários exemplos e questões usando o for e o print dos arrays. O
Correta é for x in nomes: print(x).
Gabarito: Letra E

4g.(FCC-TRF4-2019) Considere o código Python abaixo.
def oper(l, item):

pos = O
x = False

I

if l[pos] == item:

x = True else:
pos = pos+i return x v = [i, 2, 32, 8,17,19, 42,13, 0]
print(oper(v, 8))

Para que o código exiba na tela o valorTrue se o item buscado no vetor por meio da função oper for encontrado, a lacuna I deve ser corretamente preenchida por a) while pos < I and not x:
b) while pos < len(l) && x:

c) while pos < len(l) and not found(x):

d) while (pos < len(l) && not(x)):

e) while pos < len(l) and not x:

Comentários:

A função "oper" irá retornar "True" se o valor for encontrado no vetor ou
"False" caso não encontrado. Assim, é necessário que a lacuna I seja preenchida por uma estrutura de repetição while para percorrer o vetor além do " and not x" para verificar se o item buscado no vetor por meio da função "oper" foi encontrado.
Gabarito: Letra E

50.(FCC-SANASA-20ig) Uma Analista de TI está desenvolvendo um scannerde rede em Python e, para importar um recurso referente para manipulação de pacotes de rede,utilizou no programa a linha a) import pyTTS *
b) from Tkinter import *

c) import aiml *

d) from scapy.all import *

e) from numpy import *

Comentários:

Pessoal, a questão solicita um pacote para manipulação de pacotes de rede. Vejamos o que faz cada um dos comandos citados: pyTTS: biblioteca de texto para fala; Tkinter:biblioteca padrão da linguagem Python; aiml: biblioteca para inteligência artificial com aprendizado de máquina; scapy:
biblioteca que suporta envio de pacotes em rede, portanto nosso gabarito, numpy:
biblioteca para uso científico, trabalha com vetores multidimensionais.
Gabarito: Letra D

51. (FCC - TJ MA- 2019) Considere o programa Python abaixo:
numeroí = int(input('lnforme o número de Processos:'))

numero2 = int(input('lnforme o número de Juízes:'))
I

resultado = numeroí / numero2

print("Há ",resultado," processos a serem julgados por cada Juiz")
II

print("Não é possível divisão por zero")

Para tratar a exceção que será lançada se o valor contido na variável numero2 for zero, as lacunas
I e II deverão ser corretamente preenchidas por:

a) try: e catch ArithymeticException:

b) throw e catch (ZeroDivisionException $e)

c) try e catch(ArithmeticException ex)

d) throw: e catch(err)

e) try: e except ZeroDivisionError:

Comentários:

Pessoal, de imediato podemos eliminar as opções que não possuem o try. Portanto ficamos apenas com a, c e e. A questão deu a dica: "Não é possível divisão por zero". Daí podemos verificar que o gabarito é a letra E porque há uma divisão no try (resultado = numeroí / numero2).
Gabarito: Letra E

52. (FCC - TJ MA- 2019) Considere o programa Python abaixo:

I..

forx in pro:

print(x)

processos = ["0456789908", "0875643087", "0897645109"]

exibir_processos(processos)

Para que o programa seja executado corretamente, em condições ideais, a indicação I
deve ser substituída por:
/ 174

/

a) private exibir_processos(pro):

b) public exibir_processos(pro):

c) function exibir_processos(pro):

d) definition exibir_processos(pro):

e) def exibir_processos(pro):

Comentários:

Pessoal, fizemos várias questões com definição de funções, vamos relembrar?
Para criar uma função, utiliza-se a palavra-chave def. Daí já conseguimos saber que o nosso gabarito é a letra E.
Gabarito: Letra E

53. (FCC - MPE PE- 2018) Considere o fragmento de código Python abaixo.
class Cliente:

I

self.nome = nome self.renda = renda pi = Cliente("Maria", 5678.98)print(pi.nome)

print(pi.renda)

Para que o código seja compilado e executado corretamente, a lacuna I deverá ser preenchida com a) init(self, nome, renda):
b) functioninit(self, nome, renda):

c) defconstruct(self, nome, renda):

d) definit(self, nome, renda):

e) Cliente(self, nome, renda):

Comentários:

Pessoal, todas as classes possuem uma função chamadainit(), que sempre é executada quando a classe está sendo iniciada. Para que o código seja compilado e executado corretamente devemos utilizar definit(self, nome, renda):.
Gabarito: Letra D

54.(FCC -TRE SP- 2017) Considere o programa Python, abaixo,
import ..I.. as b import matplotlib.pyplot as a x = b.linspace(o, 3, 20)
y = b.linspace(o, 9, 20)
a.plot(x, y)

a.plot(x, y, 'o')
a.show()

A lacuna I deve ser preenchida corretamente com a) numpy b) matrix c) mathlab d) numberplot e) array
Comentários:

Pessoal, NumPy é uma biblioteca Python usada para trabalhar com arrays. Ela possui funções para trabalhar no domínio da álgebra linear, transformada de Fourier e matrizes.NumPy significa
Python Numérico. Para usar a linspace() é necessário importar a biblioteca NumPy.

Gabarito: Letra A

55.(FCC - PRODATER- 2016) Em Python existe um conjunto de métodos disponíveis para se trabalhar com objetos do tipo lista. Considere o trecho de programa abaixo que faz uso desses métodos.
a = [99-15, 323, 323, 2,12.5]

a.insert(2, -5)
a.append(323)
a.index(323)
a.remove(323)
a.reverse()

Ao executar este trecho de programa, o conteúdo final da lista a será:

a) [99-15, -5, 323, 2,12.5, 323]

b) [-5, 2,12.5, 99.15, 323, 323]

c) [323,12.5, 2, 323, -5, 99.15]

d) [99-15, -5, 323, 323,12.5, 2]

e) [323,323, 99-15,12.5, 2, -5]

Comentários:

Pessoal, vejamos o que cada operação gera na lista a:

a.insert(2, -5) # [99.15, 323, -5, 323, 2,12.5]

a.append(323) # [99.15, 323, -5, 323, 2,12.5, 323]

a.index(323) # [99.15, 323, -5, 323, 2,12.5, 323] (não faz nada)

a.remove(323) # [99.15, -5, 323, 2,12.5, 323] (removeu o primeiro 323)

a.reverse() # [323,12.5, 2, 323, -5, 99.15] (inverteu a lista)

Gabarito: Letra C

56.(FCC-SEMFTeresina-20i6) Considere o programa abaixo, criado na linguagem Python.
a = ['ARSETE1, 'PRODATER', 'SEMEST', 'STRANS', 'SEMAE']

I...

print i, a[i]

Considere a saída gerada pelo programa:

0ARSETE

1PRODATER

2 SEMEST

3 STRANS

4 SEMAE

Na lacuna I deve estar o comando:

a) for i in len(a):

b) foreach a as &value(a)):

c) while i<range(len(a)):

d) for i in range(len(a)):

e) for i in range(a):

Comentários:

Pessoal, o Correta a se usar quando é necessário percorrer o array é a letra d: for i in range(len(a)):
Gabarito: Letra D

57. (FCC - PGM Teresina- 2016) Considere o código-fonte abaixo, criado na linguagem Python.
def dados(n):

resultado = []
a, b = o, 1
while a < n:

/ 174

/

resultado, append(a)
a, b = b, a+b return resultado op = dados(ioo)print op

O valorfinal contido na posição de índice 6 de op é a) i b) 8
c) 5

d) 6

e) 13

Comentários:

Pessoal, é apresentado um código que gera a sequência de Fibonacci - muito cobrado em provas principalmente quando se fala em Python! A sequencia gerada é: 0,1,1, 2, 3, 5, 8,13,21, 34, 55, 89.
A posição 6 consiste do valor = 8, nosso gabarito.

Gabarito: Letra B

58.(FCC - CNMP- 2015) Considere os fragmentos de programas Phyton a seguir:
Fragmento 1:

for n in range(2,10):

forx in range(2, n):

if n % x == o:

print n, x, '*', n/x break else:
print n, 'é um número primo'
Fragmento 2:

a = ['Casa', 'Mala', 'Prova']
forx in a:

print x, len(x)

É Correta afirmar que a) o Fragmento 1 está in Correta, pois laços não podem ter uma cláusula else.
b) no Fragmento 2, a instrução for está incorreta, pois ela não pode iterar sobre a.

c) o Fragmento 1 está in Correta, pois não é possível iterar sobre sequências numéricas utilizando a função range.
d) no Fragmento 1 é verificado se o quociente da divisão de n por x corresponde a o.

e) os dois fragmentos de código estão Corretas.

Comentários:

Pessoal, ambos fragmentos estão perfeitos.

Gabarito: Letra E

5g.(FCC -TRT/MG - Técnico Judiciário - Tecnologia Da Informação) Considere o código fonte
Python abaixo.

def calcular(n):
resultado = []
a, b = 0, 1

while a < n:

I

return resultado res = calcular(100)print res

Para que seja exibido [o, i, i, 2, 3, 5, 8, 13, 21, 34, 55, 89] a lacuna "I"
precisa ser preenchida corretamente com:
a) resultado.add(a)
a, b = b, a+b b) resultado.insert(a)a, b = b, a+b c) resultado.append(a)a, b = b, a+b d) resultado.add(a)a, b - a, a+b e) resultado.append(a)a, b = a+b, b

Comentários:

Primeiro temos que saber que o Correta a ser utilizado é o append, pois queremos inserir valores a cada iteração sem perder os anteriores. Então, ficamos entre a letra (c) e (e). Em(c), temos a, b =
b, a+b equivale a a = b e b = a+b; e em (e), temos que a, b = a+b, b equivale a a = a+b e b = b.
Vamos testar a letra (e)! Antes de entrar na estrutura de repetição while, nós temos que:
a = o b = 1
Depois, temos que:

a = a + b b = b
Note que - se antes b = 1 e depois b = b - então b nunca vai mudar, b sempre será 1. Como antes a

= o e depois a = a + b, então a sempre aumentará em uma unidade. Logo, resultado em uma sequência [1, 2, 3, 4, 5, 6, 8, 9, ...]. Dessa forma, a resposta é (c)! Notem que ele se trata de umaSequência de Fibonacci.

12 iteração: resultado = [0]; a = 1; b = 1;

22 iteração: resultado = [0, 1]; a = 1; b = 2;

32 iteração: resultado = [0, 1, 1]; a = 2; b = 3;

42 iteração: resultado = [0, 1, 1, 2]; a = 3; b = 5

52 iteração: resultado = [0, 1, 1, 2, 3]; a = 5; b = 8;

62 iteração: resultado = [0, 1, 1, 2, 3, 5]; a = 8; b = 13;

72 iteração: resultado = [0, 1, 1, 2, 3, 5, 8]; a = 13; b =
2i;

82 iteração: resultado = [0, 1, 1, 2, 3, 5, 8, 13]; a = 21; b
= 34;

92 iteração: resultado = [0, 1, 1, 2, 3, 5, 8, 13, 21]; a =
34; b = 55;

10-! iteração: : resultado = = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]: ; a =
55; b = 89;

lia ! iteração: : resultado = = [0> 1, 1, 2, 3, 5, 8, 13, 21, 34,
55]; a = 89; b =

12-! iteração: : resultado = = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
89]; a = 144;

Gabarito: Letra C

6o.(FCC - 2012 - MPE/PE - Analista de Sistemas) Em Python, os métodos de lista permitem utilizar listas como pilhas, onde o item adicionado por último é o primeiro a ser recuperado. Para adicionar um item ao topo da pilha, e para recuperar um item do topo da pilha utilizam-se,respectivamente os métodos:

a) append() e pop().

b) insert() e top().

c) addTopO e pop().

d) add() e get().

e) addltemO e top().

Comentários:

append() é utilizado para adicionar um elemento no final de uma lista ou no topo de uma pilha;pop() é utilizado para recuperar um item de uma lista ou do topo de uma pilha.

Gabarito: Letra A

6i.(FCC-20i2-TRE/CE-Analista de Sistemas) Sobre Python é Correta afirmar:

a) é uma linguagem compilada, ou seja, o código-fonte de um programa é lido pelo compilador,que cria um arquivo binário, executável diretamente pelo hardware.

b) É uma linguagem fortemente tipada, ou seja, é preciso declarar variáveis e seus tipos.

c) Suporta funcionalidades comuns na orientação a objetos: herança, herança múltipla,polimorfismo, reflexão e introspecção.

d) Uma lista em Python é um conjunto de valores acessados por um índice numérico,
inteiro,
começando em 1. Assim como em outras linguagens, a lista pode armazenar apenas valores de um mesmo tipo.
e) Uma String Python é uma sequência imutável, alocada estaticamente, com restrição de tamanho.
Comentários:

(a) Errado, é uma linguagem interpretada; (b) Errado, ele realmente possui tipagem forte, mas não precisa declarar variáveis e seus tipos; (c) Correta, ele realmente suporta funcionalidades comuns da orientação a objetos como herança simples e múltipla, polimorfismo, reflexão e introspecção;
(d) Errado, a lista pode armazenar valores de tipos diferentes e começa em zero; (e)
Errado, ela não possui restrição de tamanho.
Gabarito: Letra C

/ 174

/

(Profs. Paolla Ramos e Raphael L

62.(IESES - 2015 - IFC-SC - Programação Web e Dispositivos Móveis) Sobre listas em Python
3-1-5:

a) list.remove(a) remove o primeiro item da lista cujo valor é a.

b) list.pop(a) adiciona um item de valor a ao início da lista.

c) list.append(a) adiciona um item à lista cujo índice será a.

d) Iist.index(a) retorna o valor do item cujo índice é a.

Comentários:

(a) Correta. E caso não exista o valor "a", retorna erro; (b) Errado, ele remove o item na posição "a"da lista ou - caso seja chamado sem argumento - remove o último item da lista; (c)
Errado, ele adiciona o valor "a" na última posição da lista; (d) Errado, index retorna a posição da primeira ocorrência de "a" na lista.
Gabarito: Letra A

63.OESES - 2015 - IFC-SC - Programação Web e Dispositivos Móveis) O conjunto Correta de palavras reservadas para a construção de uma estrutura de controle em Python 3.4.3 é:
a) "if", "elsif" e "else".

b) "if", "else if" e "else".

c) Somente "if"; o restante da estrutura de controle ("senão se" e
"senão") é realizado simplesmente com indentação.
d) "if", "elif"e "else".

Comentários:

A estrutura correta completa é: if, elif e else.

Gabarito: Letra D

64-(UERJ - UERJ - Analista De Sistemas - Grid) Considere 0 trecho do programa Python abaixo:def dobra (y):

x = y+ y return x x = 5dobra(x)

0 0 SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023
(Pós-Edital)

y dobra(x)printx

O valor impresso ao executarmos o programa é:

a) 5

b) io c) 15
d) 25

Comentários:

Primeiro, uma observação: as variáveis possuem escopos diferentes. Há duas ocorrências de "x" no código-fonte, mas uma está dentro do escopo local da função dobra() e o outro está fora (escopo global). Dito isso, se x = 5, temos que dobra(s). Logo, dentro do escopo dessa função, ele é recebido como y. Então, x = y + y = 5 + 5 = io. Depois, chama-se a função dobra(x)novamente, mas - dentro desse escopo-x continua igual a 5.
Logo, repetiremos o que acabamos de fazer: x = y + y = 5 + 5 = io. Por fim,
imprime-se x. Ora, o x impresso aqui tem escopo global e, não, local. Logo, ele terá valor = 5.
Gabarito: Letra A

65.(UERJ - UERJ - Analista De Sistemas) A linguagem Python possui a seguinte característica:

a) é uma linguagem compilada.

b) exige declaração de código.

c) a tupla é um tipo mutável.

d) é orientada a objetos.

Comentários:

(a) Errado, é uma linguagem interpretada; (b) Errado, não sei o que a questão quis dizer com declaração de código. Se for declaração de tipo, então não exige; (c) Errado, a tupla é equivalente a uma lista, porém imutável; (d) Correta, é realmente orientada a objetos.
Gabarito: Letra D

66. (CETAP - 2010 - AL/RR - Analista de Sistemas) Sobre a linguagem de programaçãoPYTHON, marque a alternativa INCORRETA.

a) Python suporta a maioria das técnicas da programação orientada a objetos.

b) Python suporta e faz uso constante de tratamento de exceções como uma forma de testar condições de erro e outros eventos inesperados no programa.
c) As funções são definidas em Phyton utilizando a palavra chave def.

d) A separação de blocos de código em Phyton é feita utilizando a indentação de código.

e) O operador lógico de conjunção ("e", como em a e b) é &&.

Comentários:

(a) Correta, ele realmente suporta a maioria das técnicas da programação orientada a objetos; (b)Correta, ele realmente suporta e faz uso constante de tratamento de exceções como uma forma de testar condições de erro e outros eventos inesperados no programa. Caso haja algum erro, o programa não é interrompido - o erro é tratado sem interromper o programa; (c)Correta, funções são definidas por meio da palavra-chave def; (d) Correta, a separação de blocos se dá por meio da indentação - ignorem o nome errado: é Python e, não, Phyton; (e) Errado, o operador lógico de conjunção é and e, não, &&.
Gabarito: Letra E

67.(CESGRANRIO - 2004 - SECAD/TO - Analista de Sistemas) Um programador de
Python recebeu a tarefa de criar uma função chamada calcular que recebe dois parâmetros. Para executar sua atividade, ele deve utilizar a expressão:
a) def calcular (a,b):

b) function calcular (a,b):

c) import calcular (a,b):

d) procedure calcular (a,b):

e) sub calcular (a,b):

Comentários:

Uma função é definida por meio da palavra-chave def.

Gabarito: Letra A

68. (UNIRIO - 2014 - UNIRIO) Sobre o comando range para construção de listas na linguagemPython, é CORRETA afirmar que:

a) range(4,6) gera a lista [4,5].

b) range(5) gera a lista [1,2,3,4,5].

c) range(4,6) gera a lista [4,5,6,7,8,9].

/ 174

/

d) range(5,i) gera a lista [5].

e) range(5,i,-2) gera a lista [4,5].

Comentários:

(a) Correta, range(4,6) retorna a lista [4, 5] porque não inclui o valor de índice
[6]; (b) Errado,
range(5) retorna a lista [0, 1, 2, 3, 4]; (c) Errado, já vimos que range(4,6)
retorna a lista [4, 5]; (d)
Errado, range(5,i) retorna [ ] porque o step padrão é 1 e o stop é menor que o start; (e) Errado,range(5,i,-2) retorna [5, 3] porque o step é negativo.

Gabarito: Letra A

69. (QUADRIX-2018-COREN/RS) No que se refere à linguagem de programação
Python,
assinale a alternativa correta.

a) A Python é uma linguagem de alto nível e robusta. Ela possui seu próprio framework e é incompatível com frameworks de terceiros.
b) A Python utiliza a ducktyping (tipagem dinâmica), que nada mais é do que definir um tipo para a variável, com as operações que podem ser aplicadas, antes mesmo de ela ter sido criada, com base em conhecimento prévio do programa. Esta tarefa é executada pelo interpretador.
c) O caractere marca o início de comentário. Qualquer texto depois do "/"será ignorado até o fim da linha.
d) A Python permite que os conteúdos das variáveis sejam sempre alterados, não existindo,dessa forma, tipos imutáveis.

e) Pode ser utilizada como linguagem principal no desenvolvimento de sistemas e também pode ser utilizada como linguagem script em vários softwares.
Comentários:

(a) Errado, ela realmente é uma linguagem de alto nível e robusta, mas seu framework
(coleção de pacotes e módulos de extensão) é totalmente compatível com frameworks de terceiros; (b)Errado,
ela realmente utiliza Duck Typing, mas não é necessário definir um tipo para variável antes de ela ser criada - isso pode ser inferido pelo interpretador; (c) Errado, comentários são inicializados por meio do caractere "#" e, não, (d) Errado, tipos podem ser mutáveis ou imutáveis; (e) Correta,além de ser utilizado como linguagem principal no desenvolvimento de sistemas,
o Python também é muito utilizado como linguagem script em vários softwares.
Gabarito: Letra E

7O.(IFPI - 2012 - IFPI) Com relação à linguagem de programação Python, é INCORRETA a afirmação:
a) Disponibiliza o conceito de herança múltipla, ou seja, uma classe podeter mais de uma classe pai.
b) A sintaxe Python permite o uso de somente uma instrução por linha de código. Para que seja possível colocar mais de uma, é necessário separá-las com um entretanto, essa prática é desaconselhada, visto que sua utilização prejudica a legibilidade do código.
c) Os comentários são iniciados com um caractere "#". Para fazer comentários com múltiplas linhas, utilizam-se os caracteres "#", para o início, e "#*" para o final.
d) Diferentemente de outras linguagens de programação que utilizam elementos léxicos para definir os blocos de código, a própria endentação do código é usada, em Python, para essa função.
e) Em Python, os nomes de variáveis, funções, módulos e classes são conhecidos como identificadores. O identificador_quantidade é Correta em Python.
Comentários:

(a) Correta, ele realmente possui herança múltipla, isto é, uma classe com mais de um pai; (b)Correta, Python deve ser bastante legível. É possível inserir ponto-e-vírgula para separar instruções em uma mesma linha, mas prejudica a visibilidade - o ideal mesmo é deixar somente uma instrução por linha; (c) Errado, para comentários de mais de uma linha, utiliza-se três aspas simples ou duplas;
(d) Correta, a indentação delimita blocos de código; (e) Correta, esse é um identificador válido.

Gabarito: Letra C

Questões Cespe

LISTA DE QUESTõES

í. (CESPE - DPE RO - 2022) Na linguagem Python, são consideradas sequências mutáveis as a) strings b) cadeias c) tuplas d) listas e) ranges
2. (CEBRASPE - PC PB- 2022) Na linguagem Python, o tipo de uma variável em tempo de execução é definido pelo interpretador pelo recurso denominado a) tipagem dinâmica.
b) modo interativo.

c) sintaxe.

d) interpretação bytecode.

e) empacotamento.

3. (CESPE - PC PB- 2022) Python é uma linguagem procedural que utiliza quatro tipos de dados predefinidos para lidar com coleções: conjuntos, dicionários, listas e tuplas. Arespeito desses tipos de dados, julgue os itens a seguir.
I O conjunto permite o armazenamento de uma tupla, mas não o de uma lista.

II A tupla é idêntica à lista, exceto pela forma mais simples com que sua declaração é realizada.

III A lista é um tipo de dados variável que permite a alteração de seus elementos após a sua criação.
Assinale a opção correta.

a) Apenas o item I está certo.

b) Todos os itens estão certos.

c) Apenas o item II está certo d) Apenas os itens I e III estão certos.
e) Apenas os itens II e III estão certos.

4. (CEBRASPE-(CODEVASF-2021) Na linguagem Python, as listas são coleções de qualquertipo de objetos, com exceção das próprias listas, e seus elementos são alteráveis.
5. (CEBRASPE-PF-2021) O código Python a seguir apresenta como resultado "True".
x = bool(-3)

y = bool("True"*x)
z= bool("False")
print (xandyandz)

6. (CEBRASPE - SERPRO- 2021) As tuplas, embora sejam semelhantes às listas, estão limitadas a, no máximo, cinco níveis.
7. (CEBRASPE - SERPRO- 2021) Listas são coleções alteráveis de qualquer tipo de objeto —como, por exemplo, outras listas — capazes de gerar um efeito top-down sem limite de níveis.

8. (CEBRASPE - PC DF- 2021) Com relação a mineração de dados, aprendizado de máquina e aplicações Python, julgue o item a seguir.
Uma das aplicações de Python é o aprendizado de máquina, que pode ser exemplificado por um programa de computador que aprende com a experiência de detectar imagens de armas e de explosivos em vídeos, tendo seu desempenho medido e melhorado por meio dos erros e de acertos decorrentes da experiência de detecção.
9. (CEBRASPE - BANESE- 2021) No que se refere ao pacote NumPy do Python, julgue o item subsequente. O código a seguir retorna o valor do desvio padrão amostrai do conjunto de dadosU, 2,2,3,5}

import numpy x= numpy.array([i,2,2,3,5])numpy.std(x,ddof=i)

10.(CEBRASPE - SEED PR- 2021) Em Python, quando mais de um operador aparece em uma expressão, a ordem de avaliação depende das regras de precedência de cada linguagem.Assim,
ao programar em Python, além de observar essas regras, é preciso considerar, ainda, a forma como a linguagem representa seus operadores, conforme demonstrado nos comandos a seguir.
x=7*3**2°/o4
print (x)

Assinale a opção que corresponde à saída que o compilador Python apresentará para os comandos em questão.
/ 174

/

a) i b) 3
c) 7

d) 15

e) 15-75

n.(CEBRASPE - SEED PR- 2021) Na linguagem de programação Python, existem 3
estruturas para armazenar dados indexados. A estrutura cujos valores são imutáveis depois de sua criação é conhecida como a) lista b) operador cjtupla d) classe e) dicionário
12. (CEBRASPE - PF- 2018) Considere os seguintes comandos na programação em Python.
a = " Hello, World!"

print(a.stripO)

Esses comandos, quando executados, apresentarão o resultado a seguir.

a[o]=Hello,
a[i]=World!

13. (CEBRASPE - PF- 2018) Considere o programa a seguir, na linguagem Python.
letras == ["P", "F"]

forx in letras l print(x)
A sintaxe do programa está correta e, quando executado, ele apresentará o seguinte resultado.PF

i4.(CESPE - 2013 - MPOG - Analista de Sistemas) Em Python, o comando int("i") cria um objeto do tipo int, que recebe 1 como parâmetro no seu construtor.
15. (CESPE - 2013 - MPOG - Analista de Sistemas) Em Python, o comando int("i") cria um objeto do tipo int, que recebe 1 como parâmetro no seu construtor.
16.(CESPE - 2011 - ECT - Analista de Sistemas) A linguagem Python e seu interpretador estão disponíveis para as mais diversas plataformas. Para que seja usado em determinado sistema operacional não suportado, é possível gerar o Python a partir do programa fonte utilizando um compilador C. Nesse caso, o código fonte é traduzido para o formato bytecode, que é multiplataforma e pode ser distribuído de forma independente.
17. (CESPE - 2008 - SERPRO - Analista de Sistemas) Python é uma linguagem livre de alto nível,orientada a objetos e de difícil leitura, pois não permite identação de linhas de código.

18.(CESPE - 2011 - ECT - Analista de Sistemas) A linguagem Python e seu interpretador estão disponíveis para as mais diversas plataformas. Para que seja usado em determinado sistema operacional não suportado, é possível gerar o Python a partir do programa fonte utilizando um compilador C. Nesse caso, o código fonte é traduzido para o formato bytecode, que é multiplataforma e pode ser distribuído de forma independente.
19.(CESPE - 2008 - SERPRO - Analista de Sistemas) Python é uma linguagem livre de alto nível,orientada a objetos e de difícil leitura, pois não permite identação de linhas de código.

2o.(CESGRANRIO - 2004 - SECAD/TO - Analista de Sistemas) Um programador de
Python recebeu a tarefa de criar uma função chamada calcular que recebe dois parâmetros. Para executar sua atividade, ele deve utilizar a expressão:
a) def calcular (a,b):

b) function calcular (a,b):

c) import calcular (a,b):

d) procedure calcular (a,b):

e) sub calcular (a,b):

/ 174

/

Questões FGV

2i.(FGV-TCU -2022) Considere o código Python a seguir.

def xpto(S):

for k in range(0,len(S)):
if k%2 == 0:

yield(S[k])j

S-[l,2,3,4,5,6]

for x in xpto(S[::-l]):
print (x)

A execução desse código na IDLE Shell produz, na ordem e exclusivamente, os números:

a) 6,i b) 5, 3, i c) 6, 4, 2
d) i, 3, 5

e) 2, 4, 6

22. (FGV - PC AM- 2022) Considere o código Python a seguir.

L=[o,1,1,2,3,5,8,13,21]

for k in range(o,len(l_),2):

print (L[k])

Assinale o resultado exibido pela execução desse código, na IDLE Shell 3.9.9.
a) 1, 2, 5,13

b) o, 1, 3, 8, 21,1, 2, 5,13, 21

c) 1, 3, 8, 21,1, 2, 5,13, 21

d) o, 1, 3, 8, 21

e) o, 1, 3, 8

23. (FGV- SEFAZ AM- 2022) Analise o código a seguir em linguagem de programação Python:

/ 174

/

(Profs. Paolla Ramos e Raphael L

1 def rotina(array):

for p In len(array))!
element = array[p]

wtiile ip > 0 and array[p - 1] > element:

6 ãrray(p) = arrayfp =- 1]
p -= 1

return array

13 print ( rotina{[9, 5, 31, 42, 20, 96] ) )

Ao executar esse script em um terminal, será escrito na saída padrão a) [9, 5, 3i, 42, 20, 56]
b) [8, 4, 30, 41,19, 55]

c) [56, 20, 42, 31, 5, 9]

d) [56, 42, 31, 20, 9, 5]

e) [5, 9, 20, 31, 42, 56]

24.( FGV- MPE GO- 2022) Considere o código Python a seguir.
def X(n):

if (type(N) != int):
return -1

elif (N < 1):

return o elif (N == 1):
return 1
else:

return N*X(N-i)
print (X(4))

print (X(o))

print (X(i))

print (X(i_5))
print (X("A"))

Assinale o que acontece quando esse script é executada na IDLE SheiI 3.9.9.

a) Erro de compilação, "name 'n ' is not defined"

b) Erro de compilação, "name 'N' is not defined"

c) Executa e produz resultados Corretas com quatro linhas.

d) Executa, mas produz erro de execução na quinta chamada da função X.

e) Executa, mas calcula erradamente o fatorial de 4.

25. (FGV-MPE GO-2022) Assinale a lista de números produzida pela execução, na IDLE Shell 3.9.9,
do código Python a seguir.

for x in range(-i, -io, -1):

print (x)

a) -1-2-3-4-5-6-7-8-9

b) -9 -8 -7 -6 -5 -4 -3 -2 -1

c) o-1-2-3 -4-5-6-7 -8-9

d) o -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

e) -1 -2 -3 -4 -5 -6 -7 -8 -9 -10

26.(FGV-TJDFT-2022) Analise o código Python 3.9 a seguir.
class Teste:

def self.altura = xaltura self.largura = xlargura def dimensoes(self):
print("altura = " + str(self.altura) + "\n" \ + "largura = " + str(self.largura))
x = Teste(i2, 20)

x.dimensoes()

Para que a execução desse código exiba altura = 12
largura = 20

o trecho tracejado na segunda linha deve ser substituído por:

a) init(self, xaltura, xlargura):

b) init(xaltura, xlargura):

c) init (xaltura, xlargura):

d) new (self, args[xaltura, xlargura]):

e) new (self, xaltura, xlargura):

27.(FGV-MPE SC-2022) Analise o código Python a seguir.
xi = {"A", "B", "C"}

X2 = ["AA", "BB", "CC"]

xi.add("B")

x2.append("BB")
X2.append(xi)
print (x2)

Dado que os elementos de xi podem ser exibidos em ordem aleatória, a linha que possivelmente é produzida pelo comando print na execução do código acima é:
/ 174

/

a) ['AA', 'BB', 'CC, 'BB', {'C, 'A', 'B'}]

b) ['AA', 'BB', 'CC, 'BB', 'C, 'A', 'B', 'B']

c) ['AA', 'BB', 'CC, 'BB', 'C, 'A', 'B']

d) ['AA', 'BB', 'CC, ['BB'], {'B'}]

e) {'AA','BB', 'CC,'BB','C, 'A', 'B'}

28.(FGV-MPE SC-2022) Analise o código Python a seguir.
s=o for k in range(i6,io, -2):
s-=k print (s)
O valor exibido pela execução desse trecho é:

a) o b) -28
c) -30

d) -42

e) -52

2g.(FGV-MPE SC-2022) Analise o código Python a seguir,
x = o y = 20
try:

print (y/x)
except:

print("Deu erro!")
else:

print("Ok")
finally:

print ("The end")

A saída produzida pela execução desse trecho é:

a) a) None
The end b) Deu erro!
The end c) Deu erro!Ok d) OkThe end e) NoneOk

The end

3O.(FGV-MPE SC-2022) Analise o código Python a seguir.
def xpto(L):

return (L[::-iJ)

A expressão xpto([i,2,3]) retorna:

a) []

b) [1]

c) [3]

d) [1, 2, 3]

e) [3, 2,1]

31. (FGV-MPE SC-2022) Analise o código Python a seguir.

class xptoClass:
def iter(self):
self.a = [0]
return self def next(self):self.a.append( \

self.a[-l] \

+ self.a[-2] if len(self.a) > 1 else 1)
return self.a xpto = xptoClass()xptolter = iter(xpto)

for k in range(lj6):

print(next(xptolter))

No resultado produzido pela execução do código acima, a quinta linha contém exatamente:

/ 174

/

a) [o, 1,1, 2, 2, 3]

b) [o, í, í, 2, 3, 5]

c) [0, í, 2, 3, 4, 5]

d) [o, 1, 3, 5, 7, 9l e) [1, 2, 3, 4, 5, 6]
32. (FGV- IMBEL- 2021) Analise o código Python a seguir.
x= [1,23,4,5]

print (x[::-l])

Assinale a opção que indica a saída produzida pela execução desse código.

a) [1,23,4,5]

b) 1

c) [5,1]

d) 5

e) [5,A3,2,1]

33. (FGV - IMBEL - 2021) Analise o código Python a seguir.
x= [1,23,4,5]

print (x[-i])

Assinale a opção que indica a saída produzida pela execução desse código.

a) [1,2,3,4,51

b) 1

c) [5,1]

d) 5

e) [5,4,3,2,1]

34.(FGV -TCE-AM- 2021) Considere o código Python, versão 2.7.1, na qual o comando print não requer parênteses.
def teste(n):

for k in range(lj n+1):
yield(k)

for x in teste(10):
print: x

A execução desse código:

a) não tem efeito, pois nenhum comando print é acionado;

b) provoca a exibição do número 10 na saída;

c) provoca a exibição dos números de 1 até 10 na saída;

d) provoca um erro de compilação;

e) provoca um erro de execução

35.(FGV-TJ RO-2021) Analise o código Python 2.7a seguir.
def xpto (nl, n2):

while nl != n2:

if (nl < n2):

n2 = n2 - nl else:
return nl print xpto(50j5)
nl = nl - n2

O valor exibido pelo comando print é:

a) o b) 1
c) 5

d) 10

e) 50

36.(FGV- BANESTES-2021) Considere o código Python 2.7 a seguir:
def ABC(L, n):

while True:

if len(L) >= n:

return L
else:

Lappend(len(L) ** 2)
print ABC([2o],Io)

O resultado da execução desse código é:

a) [1, 4, g, 16, 25, 36, 49, 64]

b) [1, 4, 9, 16, 25, 36, 49, 64, 81]

c) [20,1, 4, 9,16, 25, 36, 49, 64]

d) [20,1, 4, 9,16, 25, 36, 49, 64, 81]

e) [20, 4, 9,16, 25, 36, 49, 64, 81]

37. (FGV - FunSaúde CE- 2021) Observe o código Python V2.7.
def F (a, b):

while a != b:
if a > b:

a = a - b elif b > a:
b -= a return a
Assinale o valor retornado para F (48,36).

a) i b) 12
c) 24

d) 36

e) 48

38.(FGV - BANESTES- 2021) Considere o código Python a seguir.
def F(a, b, c):

for k in range(a,b):

print k ** c

Dado que uma execução da função F exibiu os números
16, 9, 4,1, o, 1,

é Correta afirmar que os valores dos parâmetros a, b, c empregados foram, respectivamente:
a) -4, í, 2;

b) -4, 2, 2;

c) -4, o, 4;

d) 4, -i, i;

e) 4, 2, 2.

39-(FGV- BANESTES-2021) Considere o código Python 2.7 a seguir.

L=[6,5,4,3,2,I]

for k in range(-3,3):

print L[k]

A execução desse código exibe os números:

a) 111654;

b) 123456;

c) 3 2 16 5 4;

d) 6 5 4 3 2 1;

e) 654654.

4O.(FGV- IMBEL- 2021) Analise o script Python 3.8 exibido a seguir.

L=["A","E","I","O","U"]

for k in range(-i, -5, -1):

print (L[k+iJ)

Assinale a saída produzida pela execução desse código.

a) AEIOU

b) A E I U

c) AUOI

d) U A E I

e) U O I E A

41.(FGV-IMBEL-2021) Analise o script Python 3.8 exibido a seguir.

L=["A","E","I","O","U"]

for k in range(o,len(L)):
print (L[4-kJ)

/ 174

/

Assinale a opção que indica a saída produzida pela execução desse código.

a) AEIOU

b) A E I O

c) E I O U

d) U O I E

e) U O I E A

42.(FGV - DPE RJ- 2019) Analise o código Python 2.7 a seguir.
frutas = ["banana","laranja"j"mangauva"]

for k in range(-l,-4,-2):
print frutas [k]

O conjunto de palavras exibidas pela execução desse código, na ordem, é:

a) banana;

b) laranja, manga;

c) uva, laranja;

d) banana, laranja, manga;

e) banana, laranja, manga;

43.(FGV- MPE AL-2018) Analise o código Python 2.7 a seguir.

Li=[]
L2=[I,2,3,4]

for k in range(3, -4,-1):

Li.append(L2[k])
forx in L:

print x

Esse programa causa a) erro de sintaxe.
b) erro de execução.

c)a exibição dos valores 43,2,1,43,2 nessa ordem.

d) a exibição do valor 4, somente.

e) a exibição dos valores 43,2,1 nessa ordem.

44-(FGV - 2015 - CM/Caruaru - Analista Legislativo - Informática) Analise o código Python a seguir.
Li=[io,20,30]
I_2=[4O,5O]

l_i.append(l_2)

print Li

Assinale a opção que descreve corretamente o que acontece quando esse programa é executado no Python 2.7:
a) Produz uma mensagem de erro, porque tenta executar uma operação inválida.

b) Exibe "[10, 20, 30, [40, 50]]".

c) Exibe "[10, 20, 30, 40, 50]".

d) Exibe "[10, 20, 30], [40, 50]".

e) Exibe "[]".

45.(FGV - 2015 -TJ/BA - Analista Judiciário) Analise o trecho de programa Python, na versão 2.7,
apresentado a seguir.

L=[I,2,3,4,5,6,7,8]

print L[::-i]

Ao ser executado, o resultado exibido é:

a) [1, 2, 3, 4, 5, 6, 7, 8]

b) [8]

c) []

d) [8, 7, 6, 5, 4, 3, 2,1]

e) [1]

46.(FGV- 2014 - MPE/AL) Analise o código Python 2.7 a seguir.

L = [10,12,14,16]

for k in range(4, -5, -1):

print L[k]

Esse programa causa:

a) erro de sintaxe.

b) erro de execução.

c) a exibição de 4 valores, 16,14,12,10, nessa ordem.

d) a exibição de 8 valores, 16,14,12,10,16,14,12,10, nessa ordem.

e) a exibição do valor 16, somente.

Questões FCC

47.(FCC- PGE AM-2O22)Em um programa escrito em Python, uma série de dados foram inseridos no array cargos, por meio da instrução abaixo.
cargos - ["Advogado","Promotor", "Procurador", "Juiz", "Desembargador", "Ministro"];

Para colocar estes dados em ordem alfabética decrescente em um novo array chamado cargos_ordenados utiliza-se a instrução:
a) for cargos_ordenados in cargos reverse True;

b) cargos_ordenados = sorted(cargos,reverse=True);

c) while cargos: cargos_ordenados = cargos- -;

d) cargos_ordenados = descending(cargos);

e) cargos_ordenados = ordered(cargos, descending=True);

48.(FCC - TRF 4 - 2019) Considerando que em um programa Python em condições ideais há um array criado pelo comando nomes = ["Maria", "Pedro", "João"], para exibir os valores contidos nesse array utiliza-se a) for x in nomes: out.print(x)
b) while x in nomes: print(x)

c) foreach x in nomes: print(x)

d) foreach x in nomes: system.println(x)

e) for x in nomes: print(x)

49-(FCC-TRF4-2019) Considere o código Python abaixo.

def oper(l, item):

pos = 0
x = False

I

if l[pos] == item:

x = True else:
pos = pos+i return x v = [1, 2, 32, 8,17,19, 42,13, o]
print(oper(v, 8))

Para que o código exiba na tela o valorTrue se o item buscado no vetor por meio da função oper for encontrado, a lacuna I deve ser corretamente preenchida por a) while pos < I and not x:
b) while pos < len(l) && x:

c) while pos < len(l) and not found(x):

d) while (pos < len(l) && not(x)):

e) while pos < len(l) and not x:

50. (FCC - SANASA- 2019) Uma Analista de TI está desenvolvendo um scanner de rede em
Python e, para importar um recurso referente para manipulação de pacotes de rede,utilizou no programa a linha a) import pyTTS *
b) from Tkinter import *

c) import aiml *

d) from scapy.all import *

e) from numpy import *

51. (FCC - TJ MA- 2019) Considere o programa Python abaixo:
numeroí = int(input('lnforme o número de Processos:'))
numero2 = int(input('lnforme o número de Juízes:'))

I

resultado = numeroí / numero2

print("Há ",resultado," processos a serem julgados por cada Juiz")

II

print("Não é possível divisão por zero")

Paratratar a exceção que será lançada se o valor contido na variável numero2 for zero, as lacunas
I e II deverão ser corretamente preenchidas por:

a) try: e catch ArithymeticException:

b) throw e catch (ZeroDivisionException $e)

c) try e catch(ArithmeticException ex)

d) throw: e catch(err)

e) try: e except ZeroDivisionError:

/ 174

/

52. (FCC - TJ MA- 2019) Considere o programa Python abaixo:
I..

forx in pro:

print(x)

processos = ["0456789908", "0875643087", "0897645109"]

exibir_processos(processos)

Para que o programa seja executado corretamente, em condições ideais, a indicação I
deve ser substituída por:
a) private exibir_processos(pro):

b) public exibir_processos(pro):

c) function exibir_processos(pro):

d) definition exibir_processos(pro):

e) def exibir_processos(pro):

53. (FCC - MPE PE- 2018) Considere o fragmento de código Python abaixo.
class Cliente:

I

self.nome = nome self.renda = renda pi = Cliente("Maria", 5678.98)print(pi.nome)

print(pi.renda)

Para que o código seja compilado e executado corretamente, a lacuna I deverá ser preenchida com a) init(self, nome, renda):
b) functioninit(self, nome, renda):

c) defconstruct(self, nome, renda):

d) definit(self, nome, renda):

e) Cliente(self, nome, renda):

54.(FCC -TRE SP- 2017) Considere o programa Python, abaixo.
import ..I.. as b import matplotlib.pyplot as a x - b.linspace(o, 3, 20)
/ 174

/

y = b.linspace(o, 9, 20)
a.plot(x, y)

a.plot(x, y, 'o')
a.show()

A lacuna I deve ser preenchida corretamente com a) numpy b) matrix c) mathlab d) numberplot e) array
55-(FCC - PRODATER- 2016) Em Python existe um conjunto de métodos disponíveis para se trabalhar com objetos do tipo lista. Considere o trecho de programa abaixo que faz uso desses métodos.
a = [99-i5, 323, 323, 2,12.5]

a.insert(2, -5)
a.append(323)
a.index(323)
a.remove(323)
a.reverse()

Ao executar este trecho de programa, o conteúdo final da lista a será:

a) [99-15, -5, 323, 2,12.5, 323]

b) [-5, 2,12.5, 99.15, 323, 323]

c) [323,12.5, 2, 323, -5, 99.15]

d) [99-15, -5, 323, 323,12.5, 2]

e) [323, 323, 99-15,12-5, 2, -5]

56.(FCC-SEMFTeresina-20i6) Considere o programa abaixo, criado na linguagem Python.
a = ['ARSETE', 'PRODATER', 'SEMEST', 'STRANS', 'SEMAE']

I...

print i, a[i]

Considere a saída gerada pelo programa:
0ARSETE

iPRODATER
2 SEMEST

3 STRANS

4SEMAE

Na lacuna I deve estar o comando:

a) for i in len(a):

b) foreach a as &value(a)):

c) while i<range(len(a)):

d) for i in range(len(a)):

e) for i in range(a):

57. (FCC - PGM Teresina- 2016) Considere o código-fonte abaixo, criado na linguagem Python.
def dados(n):

resultado = []
a, b = o, 1
while a < n:

resultado.append(a)
a, b = b, a+b return resultado op = dados(ioo)print op

O valorfinal contido na posição de índice 6 de op é a) i b) 8
c) 5

d) 6

e) 13

58.(FCC - CNMP- 2015) Considere os fragmentos de programas Phyton a seguir:
Fragmento 1:

for n in range(2,10):
forx in range(2, n):
if n % x == o:

print n, x, n/x

/ 174

/

break else:
print n, 'é um número primo'
Fragmento 2:

a = ['Casa', 'Mala', 'Prova']
forx in a:

print x, len(x)

É Correta afirmar que a) o Fragmento 1 está in Correta, pois laços não podem ter uma cláusula else.
b) no Fragmento 2, a instrução for está incorreta, pois ela não pode iterar sobre a.

c) o Fragmento 1 está in Correta, pois não é possível iterar sobre sequências numéricas utilizando a função range.
d) no Fragmento 1 é verificado se o quociente da divisão de n por x corresponde a 0.

e) os dois fragmentos de código estão Corretas.

5g.(FCC -TRT/MG - Técnico Judiciário - Tecnologia Da Informação) Considere o código fonte
Python abaixo.

def calcular(n):
resultado = []
a, b = 0, 1

while a < n:

I

return resultado res = calcular(100)print res

Para que seja exibido [o, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] a lacuna "I"
precisa ser preenchida corretamente com:
a) resultado.add(a)
a, b = b, a+b b) resultado.insert(a)a, b = b, a+b c) resultado.append(a)a, b = b, a+b d) resultado.add(a)a, b = a, a+b e) resultado.append(a)
a, b = a+b, b

6o.(FCC - 2012 - MPE/PE - Analista de Sistemas) Em Python, os métodos de lista permitem utilizar listas como pilhas, onde o item adicionado por último é o primeiro a ser recuperado. Para adicionar um item ao topo da pilha, e para recuperar um item do topo da pilha utilizam-se,respectivamente os métodos:

a) append() e pop().

b) insert() e top().

c) addTopO e pop().

d) add() e get().

e) addltemO e top().

6i.(FCC-2Oi2-TRE/CE-Analista de Sistemas) Sobre Python é Correta afirmar:

a) é uma linguagem compilada, ou seja, o código-fonte de um programa é lido pelo compilador,que cria um arquivo binário, executável diretamente pelo hardware.

b) É uma linguagem fortemente tipada, ou seja, é preciso declarar variáveis e seus tipos.

c) Suporta funcionalidades comuns na orientação a objetos: herança, herança múltipla,polimorfismo, reflexão e introspecção.

d) Uma lista em Python é um conjunto de valores acessados por um índice numérico,
inteiro,
começando em 1. Assim como em outras linguagens, a lista pode armazenar apenas valores de um mesmo tipo.
e) Uma String Python é uma sequência imutável, alocada estaticamente, com restrição de tamanho.
Questões Comentadas - Diversas Bancas

62.(IESES - 2015 - IFC-SC - Programação Web e Dispositivos Móveis) Sobre listas em Python
3-i-5:

a) list.remove(a) remove o primeiro item da lista cujo valor é a.

b) list.pop(a) adiciona um item de valor a ao início da lista.

c) list.append(a) adiciona um item à lista cujo índice será a.

d) Iist.index(a) retorna o valor do item cujo índice é a.

63.OESES - 2015 - IFC-SC - Programação Web e Dispositivos Móveis) O conjunto Correta de palavras reservadas para a construção de uma estrutura de controle em Python 3.4.3 é:
a) "if", "elsif" e "else".

b) "if", "else if" e "else".

c) Somente "if"; o restante da estrutura de controle ("senão se" e
"senão") é realizado simplesmente com indentação.
d) "if", "elif"e "else".

64.(UERJ - UERJ - Analista De Sistemas - Grid) Considere o trecho do programa Python abaixo:
def dobra (y):

x = y + y return x x = 5dobra(x)
dobra(x)
printx

O valor impresso ao executarmos o programa é:

a) 5

b) 10

c) 15

d) 25

65.(UERJ - UERJ - Analista De Sistemas) A linguagem Python possui a seguinte característica:

/ 174

/

a) é uma linguagem compilada.

b) exige declaração de código.

c) a tupla é um tipo mutável.

d) é orientada a objetos.

66. (CETAP - 2010 - AL/RR - Analista de Sistemas) Sobre a linguagem de programaçãoPYTHON, marque a alternativa INCORRETA.

a) Python suporta a maioria das técnicas da programação orientada a objetos.

b) Python suporta e faz uso constante de tratamento de exceções como uma forma de testar condições de erro e outros eventos inesperados no programa.
c) As funções são definidas em Phyton utilizando a palavra chave def.

d) A separação de blocos de código em Phyton é feita utilizando a indentação de código.

e) O operador lógico de conjunção ("e", como em a e b) é &&.

67.(CESGRANRIO - 2004 - SECAD/TO - Analista de Sistemas) Um programador de
Python recebeu a tarefa de criar uma função chamada calcular que recebe dois parâmetros. Para executar sua atividade, ele deve utilizar a expressão:
a) def calcular (a,b):

b) function calcular (a,b):

c) import calcular (a,b):

d) procedure calcular (a, b):

e) sub calcular (a,b):

68. (UNIRIO - 2014 - UNIRIO) Sobre o comando range para construção de listas na linguagemPython, é CORRETA afirmar que:

a) range(4,6) gera a lista [4,5].

b) range(5) gera a lista [1,23,4,5].

c) range(4,6) gera a lista [4,5,6,7,8,9].

d) range(5,i) gera a lista [5].

e) range(5,i,-2) gera a lista [4,5].

69. (QUADRIX-2018-COREN/RS) No que se refere à linguagem de programação
Python,
assinale a alternativa correta.

a) A Python é uma linguagem de alto nível e robusta. Ela possui seu próprio framework e é incompatível com frameworks de terceiros.
b) A Python utiliza a duck typing (tipagem dinâmica), que nada mais é do que definir um tipo para a variável, com as operações que podem ser aplicadas, antes mesmo de ela ter sido criada, com base em conhecimento prévio do programa. Esta tarefa é executada pelo interpretador.
c) O caractere marca o início de comentário. Qualquer texto depois do "/''será ignorado até o fim da linha.
d) A Python permite que os conteúdos das variáveis sejam sempre alterados, não existindo,dessa forma, tipos imutáveis.

e) Pode ser utilizada como linguagem principal no desenvolvimento de sistemas e também pode ser utilizada como linguagem script em vários softwares.
7O.(IFPI - 2012 - IFPI) Com relação à linguagem de programação Python, é INCORRETA a afirmação:
a) Disponibiliza o conceito de herança múltipla, ou seja, uma classe podeter mais de uma classe pai.
b) A sintaxe Python permite o uso de somente uma instrução por linha de código. Para que seja possível colocar mais de uma, é necessário separá-las com um entretanto, essa prática é desaconselhada, visto que sua utilização prejudica a legibilidade do código.
c) Os comentários são iniciados com um caractere "#". Para fazer comentários com múltiplas linhas, utilizam-se os caracteres "#", para o início, e "#*" para o final.
d) Diferentemente de outras linguagens de programação que utilizam elementos léxicos para definir os blocos de código, a própria endentação do código é usada, em Python, para essa função.
e) Em Python, os nomes de variáveis, funções, módulos e classes são conhecidos como identificadores. O identificador_quantidade é Correta em Python.
/ 174

/

GABARITo í. Letra D 26.Letra A51. Letra E

2. Letra A 27.Letra A
52. Letra E

3. Letra D 28.Letra D
53. Letra D

4. Errado 29.Letra B
54. Letra A

5. Errado 30. Letra E
55. Letra C

6. Errado 31. Letra B
56. Letra D

7. Correta 32. Letra E
57. Letra B

8. Correta 33. Letra D
58. Letra E

9. Correta 34. Letra C
59. Letra C

10. Letra B 35. Letra C
60.Letra A

11. Letra C 36. Letra D
61. Letra C

12. Errado 37. Letra B
62.Letra A

13. Errado 38. Letra B
63. Letra D

14. Correta 39. Letra C
64.Letra A

15. Correta 40. Letra C
65. Letra D

16. Correta 41. Letra E
66. Letra E

17. Errado 42. Letra C
67. Letra A

18. Correta 43. Letra B
68. Letra A

19.Errado 44. Letra B
69. LetraE

20. Letra A 45. Letra D
70. Letra C

21. Letra C 46.Letra A

22. Letra D 47. Letra B

23. Letra E 48.Letra E

24. Letra B 49.Letra E

25. Letra A 50.Letra D

FRAMEWoRkS PYTHoN: DJANGo

Conceitos Básicos

Django é um framework de aplicação web, open source e escrito na linguagemPython. Ele usa a estrutura de design
MVT (MVT significa ModelView
Template]. Devido ao seu recurso de desenvolvimento rápido. 0 Django é muito exigente no mercado atual.
Leva menos tempo para construir qualquer tipo de aplicativo. Por que dizemos este
Model View
Template porque este framework funcionará baseado no modelo como um banco de dados e a visualização como uma funcionalidade de controle; e o template funcionará como um lado do usuário para interação de comunicação.
Django é um framework web Python de alto nível que encoraja o desenvolvimento rápido e design limpo e pragmático. Construído por desenvolvedores experientes, ele resolve grande parte dos problemas do desenvolvimento na Web, para que você possa se concentrar em escrever seu aplicativo sem precisar reinventar a roda. É gratuito e de código aberto.
De acordo com o site do framework, Django é "Ridiculamente rápido" e foi projetado para ajudar os desenvolvedores a levar os aplicativos do conceito à conclusão o mais rápido possível.Ademais, é tranquilamente seguro tendo em vista que leva a segurança a sério e ajuda os desenvolvedores a evitar muitos erros comuns de segurança.
Por fim, é excessivamente escalável, já que alguns dos sites mais movimentados da web,
como
Spotify, Youtube, Dropbox, Pinterest Instagram, NASA, National Geographic entre outros aproveitam a capacidade do Django de escalar de forma rápida e flexível.
Como o Django foi desenvolvido em um ambiente de redação de ritmo acelerado, ele foi projetado para tornar as tarefas comuns de desenvolvimento da Web rápidas e fáceis.
[aqui]

Para conhecer a estrutura MVT do Django primeiro precisamos saber o que é a estrutura
MVT. A
forma completa do MVT é o Model View Template. A estrutura MVT tem três partes 1.
Modelo 2.
Visão 3. Template.

* Model: Esta parte da estrutura MVC atua como um meio para armazenar dados do usuário no banco de dados. Ele é responsável por lidar com a parte lógica da aplicação web, bem como como os dados são armazenados no banco de dados.
/ 174

/

* Views: Esta é uma interface de usuário. Ele é responsável por exibir os dados dos bancos de dados e armazenar as informações fornecidas pelo usuário. No Django as visualizações não são as mesmas que são na estrutura básica do MVC.
* Controlador: Esta parte no MVC é responsável por toda a lógica e funcionamento por trás da aplicação web. Quando um usuário levanta uma solicitação HTTP, o controlador recebe a solicitação e envia de volta a resposta apropriada.
Django

User

Template

-

Portanto, o Django implementa um tipo diferente de arquitetura MVT! O MVT
(Model View
Template) é um padrão de projeto de software. Em termos simples, o modelo ajuda a lidar com banco de dados. É uma camada de acesso a dados que lida com os dados. O Template é uma camada de apresentação que trata completamente da parte da interface do usuário. A View é usada para executar a lógica de negócios e interagir com um modelo para transportar dados e renderizar umTemplate.

Embora o Django siga o padrão MVC, ele mantém suas próprias convenções. Assim, o controle é tratado pelo próprio framework. Não há controlador separado e o aplicativo completo é baseado em Model View e Template. Por isso é chamado de aplicativo MVT.
Mas por que o Django usa o modelo MVT, por que não usa o MVC? Na interpretação dos desenvolvedores do framework, a "visão" descreve os dados que são apresentados ao usuário. Não é necessariamente a aparência dos dados, mas quais dados são apresentados. Avisualização descreve quais dados você vê, não como você os vê. É uma distinção sutil.
Portanto, em nosso caso, uma "view" é a função de retorno de chamada do Python para uma URLespecífica, porque essa função de retorno de chamada descreve quais dados são apresentados.

/ 174

/

Além disso, é sensato separar o conteúdo da apresentação - que é onde os templates entram. NoDjango, uma "view" descreve quais dados são apresentados, mas uma view normalmente delega a um template, que descreve como os dados são apresentados.
Onde o "controlador" se encaixa, então? No caso do Django, provavelmente é o próprio framework:
o maquinário que envia uma requisição para a view apropriada, de acordo com a configuração de
URL do Django.

i (CESPE - SEFAZ CE- 2021) Com relação à arquitetura de desenvolvimento de software, julgue o i i item a seguir.
i O framework Django utiliza a estrutura MTV (model-template-view), sendo template a camada i i de apresentação, em que as informações são visualizadas pelos usuários.
i Comentários: Vamos relembrar? 0 modelo ajuda a lidar com banco de dados. É uma camada de i i acesso a dados que lida com os dados. O Template é uma camada de apresentação que trata iÊ completamente da parte da interface do usuário. A View é usada para executar a lógica de i i negócios e interagir com um modelo para transportar dados e renderizar umTemplate. i i Portanto, correta questão. (Gabarito: Correto)
A rapidez no desenvolvimento utilizando Django é modelada de acordo com o princípio
DRY -
Dont Repeat Yourself, evitando ao máximo códigos duplicados e gerando um ganho de agilidade excelente no ciclo de desenvolvimento web.
Django utiliza MVC e outros padrões, muito bem aceitos por toda a comunidade, em sua filosofia de desenvolvimento, o que leva a fácil manutenção, melhor legibilidade dos códigos e simplicidade.
Django é formado pelos principais componentes necessários para um framework web e muito mais, como mapeamento objeto relacional, sistema de administração, sistema de templates,sistema de cache, suporte para internacionalização e mapeamento elegante de uris.

Todos os componentes são altamente integrados, já que os componentes não são de terceiros,proporcionando ótima integração entre as partes do framework, com maior coerência e coesão.

Características

* Mapeamento objeto-relacional - é possível definir seus modelos de dados com classes emPython e gerar automaticamente o SQL correspondente e executá-lo no banco de dados a ser utilizado. Mas, se por preciso é possível escrever os comandos SQL também.
* Interface de administração automática - o Django traz uma interface de administração automática onde é possível atualizar o conteúdo do seu sistema.
* Uris elegantes - é possível projetar URLs sem nenhuma limitação estrutural.

* Sistema de templates - o django contém um sistema de templates que separa o html do codigo em Python.
* Internacionalização - esse framework tem suporte a aplicações multi-linguagem.

/ 174

/

* NewForms - é possível gerar e manipular formulários facilmente através dos modelos de dados definidos.
* Unicode - suporta o unicode, de forma simples

Embora você possa usar o Django sem um banco de dados, ele vem com um mapeador objeto-relacional no qual você descreve o layout do banco de dados em código Python.

A sintaxe do modelo de dados oferece muitas maneiras ricas de representar seus modelos
- até agora, ela tem resolvido muitos anos de problemas de esquema de banco de dados.
Como usar?

O modelo Django funcionará como gerenciamento de banco de dados, usamos dois comandos como: -python manage.py makemigrations O Django irá deduzir as alterações no arquivo models.py e pronto para enviar os dados para o sqlite3 (escolha qualquer banco de dados]. Em seguida, fazemos o python manage.py migrar, então o sistema Django irá salvar todas as mudanças em seu sistema de banco de dados. Então nós fazemos mais um comando Python manage.py run server no final isso irá iniciar nosso projeto e nos dará o endereço localhost para o projeto rodando localmente. E o arquivo views.py tratará da solicitação do projeto para a chamada da API para o gerenciamento de modelos nas solicitações, podemos escrever as visualizações na forma de funções python.
O Django suporta oficialmente os seguintes bancos de dados:

* PostgreSQL

* MariaDB

* MySQL

* Oracle

* SQLite

Importante! Bancos de dados NoSQL não são oficialmente suportados pelo próprio Django.
Existem, no entanto, vários projetos paralelos e bifurcações que permitem a funcionalidadeNoSQL no Django, como Django non-rel.

Há também vários backends de banco de dados fornecidos por terceiros. O
Django tenta suportar o maior número possível de recursos em todos os backends de banco de dados.No entanto, nem todos os back-ends de banco de dados são iguais e foram tomadas decisões de design sobre quais recursos oferecer suporte.
Este arquivo descreve alguns dos recursos que podem ser relevantes para o uso do
Django. Não se destina a substituir a documentação específica do servidor ou os manuais de referência.
O arquivo settings.py contém todas as configurações do projeto junto com os detalhes da conexão do banco de dados. Por padrão, o Django trabalha com SQLite, banco de dados e permite a configuração para outros bancos de dados também.
/ 174

/

A conectividade do banco de dados requer todos os detalhes da conexão, como nome do banco de dados, credenciais do usuário, nome da unidade do nome do host, etc.
Para conectar com o MySQL, o driver django.db.backends.mysql é usado para estabelecer uma conexão entre o aplicativo e o banco de dados. Vamos ver um exemplo. Precisamos fornecer todos os detalhes da conexão no arquivo de configurações.
0 Django pode ser implantado no Oracle Container Engine for Kubernetes (OKE)
e aproveitar a resiliência e a agilidade do Kubernetes sem a necessidade de gerenciar um cluster do Kubernetes. Para simplificar ainda mais sua implantação do Django, você pode usar um dos muitos serviços de banco de dados gerenciados fornecidos pelo Oracle Cloud Infrastructure(OCI).

0 Django abre uma conexão com o banco de dados quando faz uma consulta ao banco de dados pela primeira vez. Ele mantém essa conexão aberta e a reutiliza em solicitações subsequentes.0 Django fecha a conexão quando ela excede a "idade máxima" definida por "CONN_MAX_AGE"
ou quando não é mais utilizável.

Em detalhes, o Django abre automaticamente uma conexão com o banco de dados sempre que precisar e ainda não tiver uma - seja porque esta é a primeira conexão, ou porque a conexão anterior foi fechada.
No início de cada solicitação, o Django fecha a conexão se ela atingir sua idade máxima. Se seu banco de dados encerrar conexões ociosas após algum tempo, você deve definirCONN_MAX_AGEum valor menor, para que o Django não tente usar uma conexão que foi encerrada pelo servidor de banco de dados. (Esse problema pode afetar apenas sites de tráfego muito baixo.)
No final de cada solicitação, o Django fecha a conexão se ela atingiu sua idade máxima ou se estiver em um estado de erro irrecuperável. Se algum erro de banco de dados ocorreu durante o processamento das requisições, o Django verifica se a conexão ainda funciona e a fecha se não funcionar. Assim, os erros de banco de dados afetam no máximo uma solicitação por thread de trabalho de cada aplicativo; se a conexão se tornar inutilizável, a próxima solicitação obtém uma nova conexão.
A configuração CONN_HEALTH_CHECKSpara Truepode ser usada para melhorar a robustez da reutilização da conexão e evitar erros quando uma conexão foi fechada pelo servidor de banco de dados que agora está pronto para aceitar e servir novas conexões, por exemplo,após a reinicialização do servidor de banco de dados. A verificação de integridade é realizada apenas uma vez por solicitação e somente se o banco de dados estiver sendo acessado durante o tratamento da solicitação.
Modelos Django

/ 174

/

Um modelo é a fonte única e definitiva de dados sobre seus dados. Ele contém os campos e comportamentos essenciais dos dados que você está armazenando. Geralmente, cada modelo é mapeado para uma única tabela de banco de dados.
O Django define uma API padrão para carregar e renderizar templates independente do backend. O carregamento consiste em encontrar o modelo para um determinado identificador e pré-processá-lo, geralmente compilando-o em uma representação na memória.Renderizar significa interpolar o modelo com dados de contexto e retornar a string resultante.
Templates Django

Django fornece uma maneira fácil de criar HTML poderoso usando seu programa de template.Os templates do Django são criados normalmente usando HTML, CSS e Javascript. O
template
Django gerencia bem e produz páginas HTML que são visíveis para o usuário final.

A função Template basicamente tem três parâmetros:

1. Request: Solicitação Inicial.

2. O Caminho para criar templates - Existe a opção TEMPLATE_DIRS relacionada às variáveis projectpy que estão mudando.
3. Dicionário de Parâmetros - Um dicionário que contém todo e qualquer elemento necessário para o template.
Trabalhando com formulários django.forms é a biblioteca de manipulação de formulários. Embora seja possível processar submissões de formulário somente usando a classe HttpRequest do Django, usando a biblioteca de formulários fica melhor para a realização de uma série de tarefas comuns relacionadas a formulários. Usando-o, você pode:
1. Mostrar um formulário HTML com widgets gerados automaticamente.

2. Verificar os dados submetidos conforme um conjunto de regras de validação.

3. Re-exibir um formulário no caso de haver erros de validação.

4. Converter dados de formulários submetidos a tipos relevantes do Python.

A biblioteca trabalha com os seguintes conceitos:

Conceito | Descrição

Uma classe que corresponde a um widget de formulário

Widget

Field

HTML, e.g. cinput type="text"> ou <textarea>. Este manipula a renderização do widget como HTML.
Uma classe que é responsável por fazer validação, e.g. um
EmailField que assegura-se de que seu dado é um endereço de e-mail válido.
/ 174

/

Form
Form Media

Uma coleção de campos que sabem como validar e mostrar a si mesmo como HTML.
Os recursos CSS e Javascript que são requeridos pa renderizar um formulário.
A biblioteca é dissociada de outros componentes do Django, como a camada de banco de dados, views e templates. Ele invoca somente do Django settings, algumas funções helpers django.utils e hooks de internacionalização do Django (mas você não é obrigado a usar internacionalização para usar esta biblioteca].
A linguagem de template do Django

A linguagem de template do Django é projetada para encontrar um equilíbrio entre poder e facilidade. Ele foi projetado para ser confortável para aqueles acostumados a trabalhar comHTML. Se você tiver alguma exposição a outras linguagens de template baseadas em texto, como
Smarty ou CheetahTemplate , você deve se sentir em casa com os templates do Django.

Se você tem experiência em programação, ou se está acostumado com linguagens que misturam código de programação diretamente em HTML, você deve ter em mente que o sistema de template Django não é simplesmente Python embutido em HTML. Isso ocorre por design:o sistema de modelo destina-se a expressar a apresentação, não a lógica do programa.
Portanto, Django contém um sistema de templates que busca separar o html do código em
Python.

Um modelo é simplesmente um arquivo de texto. Ele pode gerar qualquer formato baseado em texto (HTML, XML, CSV, etc.). Já, um template contém variáveis, que são substituídas por valores quando o template é avaliado, e tags, que controlam a lógica do template.
As variáveis ficam assim: {{ variable }}. Quando o mecanismo de modelo encontra uma variável,
ele avalia essa variável e a substitui pelo resultado. Usa-se um ponto (.) para acessar os atributos de uma variável.
Se você usar uma variável que não existe, o sistema de modelo inserirá o valor da configuraçãoTEMPLATE_STRINGJFJNVALID, que é definida como " (a string vazia) por padrão.

Views genéricas

Escrever aplicações web pode ser monótono, porque nós repetimos certos padrões várias e várias vezes. O Django tenta tirar um pouco dessa monotonia nas camadas de model e template,mas os desenvolvedores web também experimentam esse tédio na camada da view.

/ 174

/

As views genéricas do Django foram criadas para diminuir esse sofrimento. Elas pegam padrões comuns encontrados no desenvolvimento web e abstraem eles, assim você pode escrever rapidamente views comuns sem ter que escrever muito código.
Podemos identificar algumas tarefas comuns, como mostrar uma lista de objetos, e escrever código que mostre uma lista de qualquer objeto. Então, o model em questão pode ser passado como um argumento extra ao URLconf.
0 Django vem com views genéricas que fazem o seguinte:

* Efetuam "simples" tarefas comuns: redirecionar para uma página diferente e renderizar determinado template.
* Mostrar uma lista e página com detalhes de um único objeto. Se estamos criando uma aplicação para gerenciar conferências, então uma view talkjist e uma view registered_user_list seriam exemplo de views de listas. Uma única página de conversa seria o que chamamos de view de "detalhe" .
* Apresentar objetos baseados em data em páginas categorizadas por ano/mês/dia, os detalhes associados, e as "últimas" páginas. Os arquivos por ano, mês e dia do Blog daDjango Brasil [http://www.djangobrasil.org/weblog/] foram construídos com nessas views,
como exemplo de um típico arquivo de jornal.

* Permitir usuários a criar, atualizar e deletar objetos - com ou sem autorização.

Juntas, essas views oferecem uma interface fácil para realizar as tarefas mais comuns que os desenvolvedores encontram.
Gerenciando arquivos

Por padrão, o Django armazena arquivos localmente, usando as configurações MEDIA_ROOT e
MEDIA_URL. No entanto, o Django provê formas de se criar um sistema de armazenamento customizado, que permite você personalizar completamente, onde e como o Django armazena arquivos..
Quando você usa um FileField ou ImageField, o Django provê um conjunto de APIs que você pode usar para negociar com este arquivo.
Internamente, o Django usa um django.core.files.File toda vez que ele precisa representar um arquivo. Este objeto é um pequeno contorno ao objeto file nativo do Python com algumas adições específicas do Django. Na maior parte do tempo você simplesmente irá usar um File que o Django fornece a você.
Por trás das cenas, o Django se encarrega das decisões sobre como e onde os arquivos são armazenados no sistema de arquivos. Este é um objeto que na verdade entende coisas como sistema de arquivos, abertura e leitura de arquivos, etc.
/ 174

/

O sistema de armazenamento padrão do Django é dado pela configuraçãoDEFAULT_FILE_STORAGE; se você não provê explicitamente um sistema de armazenamento,
é este que será utilizado.

Testando aplicações Django

O teste automatizado é uma ferramenta extremamente útil para eliminar bugs utilizada pelo desenvolvedor Web moderno. Você pode usar uma coleção de testes - uma test suite -para resolver, ou evitar, vários problemas:
Quando você está escrevendo um código novo, pode usar os testes para verificar se seu código funciona como esperado. Quando está refatorando ou modificando um código antigo, você pode usar os testes para garantir que suas mudanças não afetaram inesperadamente o comportamento de sua aplicação.
Testar uma aplicação Web é uma tarefa complexa, porque uma aplicação Web é feita de várias camadas de lógica - da manipulação de uma requisição em nível HTTP, para a validação e processamento de formulário, para a renderização de templates. Com o framework de teste-execução do Django e outros utilitários, você pode simular requisições, inserir dados de teste,inspecionar a saída de sua aplicação e frequentemente verificar se seu código está fazendo o que deveria.
Autenticação de Usuário no Django

O Django vem com um sistema de autenticação de usuário. Ele manipula contas de usuário,grupos, permissões e sessões de usuário baseados em cookie. O sistema de autenticação consiste em:
* Usuários

* Permissões: Flags binário (yes/no) designando quando um usuário pode executar uma certa tarefa.
* Grupos: Uma forma genérica de aplicar labeis e permissões para mais de um usuário.

* Mensagens: Uma forma simples de enfileirar mensagens para um dado usuário.

O framework de cache do Django

Um dilema essencial dos sites dinâmicos vem a ser o próprio fato de serem dinâmicos. Cada vez que um usuário requisita uma página, o servidor web faz todo o tipo de cálculos -consultas a bancos de dados, renderização de templates e lógica de negócio - para criar a página que o seu visitante vê. Isso tem um custo de processamento muito maior que apenas a leitura de arquivos estáticos no disco.
Para a maior parte dos aplicativos Web, esse overhead não é um problema. A maior parte das aplicações Web não são o washingtonpost.com oouslashdot.org; são simplesmente sites
/ 174

/

pequenos a médio com tráfico equivalente. Mas para aplicações de porte médio para grande, é essencial eliminar toda a sobrecarga possível.
É onde entra o cache. Fazer o cache de algo é gravar o resultado de um cálculo custoso para que você não tenha de executar o cálculo da próxima vez.
O Django vem com um sistema de cache robusto que permite que você guarde as páginas dinâmicas para que elas não tenham de ser calculadas a cada requisição. Por conveniência,Django oferece diferentes níveis de granularidade de cache: Você pode fazer o cache da saída de views específicas, você pode fazer o cache somente das partes que são difíceis de produzir,ou pode fazer o cache do site inteiro.

O Django também trabalha com caches do tipo "upstream" , como o
Squid
[http://www.squid-cache.org/] e cache baseado em navegador. Esses são tipos de cache que você não controla diretamente.
Internacionalização

0 Django tem um suporte completo para internacionalização dos textos dos códigos e templates.
0 objetivo da internacionalização é permitir que uma única aplicação web ofereça seus conteúdos e funcionalidades em múltiplas linguagens.
0 desenvolvedor Django, pode conseguir isto adicionando uns poucos hooks ao seu código

Python e templates. Estes hooks, chamados translation strings, dizem ao Django: "Este texto deve ser traduzido para o idioma do usuário, se a tradução para este texto estiver disponível nesta língua."
0 Django se preocupa em usar estes hooks para traduzir as aplicações Web, em tempo de execução, conforme as preferências de idioma do usuário. Essencialmente, o Django faz duas coisas:
1. Permite que o desenvolvedor ou autor de templates especifique quais partes de sua aplicação podem ser traduzidas.
2. Usa os hooks para traduzir a aplicação web para um usuário em particular de acordo com sua preferência.
Sinais (Signals)

0 Django incluí um "dispachador de sinal" que ajuda ao permitir que aplicações dissociadas sejam notificadas quando uma ação ocorre em qualquer lugar do framework. Em resumo,sinais permitem certos remetentes notificar um conjunto de receptores sobre alguma ação que tenha ocorrido. Eles são especialmente úteis quando muitas peças de código podem estar interessados nos mesmos eventos.
/ 174

/

O Django fornece um conjunto de sinais embutidos que deixam o código do usuário ser notificado pelo próprio Django sobre certas ações. Estas incluem algumas notificações úteis:
Sinal | Descrição django.db.models.signals.pre_save &django.db.models.signals.post_save django.db.models.signals.pre_delete&

django.db.models.signals.post_delete django.core.signals.request_started
&

django.core.signals.request_finished

Enviado antes ou depois que um método de model savef) é chamado.
Enviado antes ou depois que um método de model deleteO é chamado.
Enviado quando o Django inicia ou finaliza uma requisição HTTP.
Escrevendo seu primeiro aplicativo Django

Para usar pela primeira o Django, você terá que cuidar de algumas configurações iniciais. Ou seja, você precisará gerar automaticamente algum código que estabeleça um projeto Django-
uma coleção de configurações para uma instância do Django, incluindo configuração de banco de dados, opções específicas do Django e configurações específicas do aplicativo.
Na linha de comando, cd em um diretório onde você gostaria de armazenar seu código,
execute o seguinte comando:
$ django-admin startproject mysite

Após exeutar esse comando será criado seu projeto contendo:

mysite/

manage.py mysite/
init.py settings.py uris.py asgi.py wsgi.py
Arquivo | Descrição

0 diretório raiz externo é um contêiner para seu mysite/
projeto. Seu nome não importa para o Django; você pode renomeá-lo para o que quiser.
/ 174

/

manage.py mysite/_init_.py mysite/settings.py
Um utilitário de linha de comando que permite interagir com este projeto Django de várias maneiras.Você pode ler todos os detalhes manage.pyem django-
admin e manage.py.

um arquivo vazio que informa ao Python que esse diretório deve ser considerado um pacote do Python.Se você é um iniciante em Python, leia mais sobre pacotes nos documentos oficiais do Python.
Configurações/configuração para este projeto

Django. As configurações do Django lhe dirão tudo sobre como as configurações funcionam.
As declarações de URL para este projeto Django; uma
"tabela de conteúdo" do seu site com Django.

Um ponto de entrada para servidores web compatíveis com ASGI para atender seu projeto.
Um ponto de entrada para servidores web compatíveis com WSGI para atender seu projeto.
O diretório interno mysite/é o pacote Python real para seu projeto. Seu nome é o nome do pacote Python que você precisará usar para importar qualquer coisa dentro dele (por exemplo,mysite.urls).

(Pró-Reitoria GP CP2 - CP II- 2017) Django é um framework voltado para o desenvolvimento web que utiliza a Linguagem Python.
Partindo da premissa que temos o Django instalado e que você já está posicionado dentro do diretório onde deseja iniciar seu projeto, o comando para a sua criação é:
a] $ django-admin mysite b) $ django-admin mysite startnew c] $ django-admin startproject mysite d) $ django-admin startnewproject "mysite"
Comentários: Para iniciar seu projeto, o comando para a sua criação é: $
django-admin startproject mysite (Gabarito: Letra C)
/ 174

/

Memcached

0 tipo de cache mais rápido e eficiente suportado nativamente pelo Django, o Memcached é um servidor de cache totalmente baseado em memória, originalmente desenvolvido para lidar com altas cargas no Livejournal.com e, posteriormente, de código aberto pela DangaInteractive.
Ele é usado por sites como Facebook e Wikipedia para reduzir o acesso ao banco de dados e aumentar drasticamente o desempenho do site.
0 Memcached é executado como um daemon e recebe uma quantidade especificada de RAM.
Tudo o que ele faz é fornecer uma interface rápida para adicionar, recuperar e excluir dados no cache. Todos os dados são armazenados diretamente na memória, portanto, não há sobrecarga de banco de dados ou uso do sistema de arquivos.
RESUMO

Model -> responsável por mapear o banco de dados para o projeto.

Template -> é responsável por toda a visualização dos dados, é a camada responsável pela apresentação dos dados, as interfaces gráficas, por exemplo, ou ainda o local em que vai o HTML.View -» é a camada que traz consigo a lógica do negócio. É o que determina o que vai acontecer no projeto.
/ 174

/

FRAMEWoRkS PYTHoN: FLASk

Conceitos Básicos web development,one drop at a time

Flask é um framework web. Isso significa que o flask fornece ferramentas, bibliotecas e tecnologias que permitem criar um aplicativo da web. Este aplicativo da web pode ser páginas da web, um blog, um wiki ou um aplicativo de calendário baseado na web ou um site comercial. Flask é um framework web leve escrita em Python e baseado no kit de ferramentas WSGI e no mecanismo de modeloJinja2. Flask faz parte das categorias do micro-framework. Micro-frameworks são normalmente frameworks com pouca ou nenhuma dependência de bibliotecas externas.
O Flask é um framework pequeno pela maioria dos padrões - pequeno o suficiente para ser chamado de "micro-framework" e pequeno o suficiente para que, assim que você se familiarizar com ele,provavelmente seja capaz de ler e entender todo o seu código-fonte.

Mas ser pequeno não significa que ele faça menos que outros frameworks. O Flask foi projetado como uma estrutura extensível desde o início; ele fornece um núcleo sólido com os serviços básicos,enquanto as extensões fornecem o resto. Como você pode escolher os pacotes de extensão que deseja, você acaba com uma pilha enxuta que faz exatamente o que você precisa.
Flask tem três dependências principais. Os subsistemas de roteamento, depuração e Web Server
Gateway Interface (WSGI) vêm de Werkzeug; o suporte de modelo é fornecido por Jinja2; e a integração da linha de comando vem do Click. Essas dependências são todas de autoria de ArminRonacher, o autor do Flask.

O Flask não tem suporte nativo para acessar bancos de dados, validar formulários da web, autenticar usuários ou outras tarefas de alto nível. Esses e muitos outros serviços importantes que a maioria dos aplicativos da Web precisam estão disponíveis por meio de extensões que se integram aos pacotes principais. Como desenvolvedor, você tem o poder de escolheras extensões que funcionam melhor para o seu projeto ou até mesmo escrever as suas próprias, se desejar. Isso contrasta com uma estrutura maior, em que a maioria das escolhas foram feitas para você e são difíceis ou às vezes impossíveis de fazer mudança. Características do Flask:
* Suportes integrados para testes de unidade;

* Usa modelagem Jinja2;

* Suporte para Cookies seguros;

/ 174

/

* Extensa documentação;

* Compatibilidade do Google App Engine.

O Flask se destaca de outras estruturas porque permite que os desenvolvedores assumam o controle e tenham total controle criativo de seus aplicativos. Talvez você já tenha ouvido a frase "combater a estrutura" antes. Isso acontece com a maioria dos frameworks quando você decide resolver um problema com uma solução que não é a oficial. Pode ser que você queira usar um mecanismo de banco de dados diferente ou talvez um método diferente de autenticação de usuários.Desviar-se do caminho definido pelos desenvolvedores do framework lhe dará muitas dores de cabeça.
Flask não é assim. Você gosta de bancos de dados relacionais? Excelente. Flask suporta todos eles.
Talvez você prefira um banco de dados NoSQL? Não há problema algum. Flask também trabalha com NoSQL. Quer usar seu próprio mecanismo de banco de dados caseiro? Não precisa de um banco de dados? Continua tudo bem. Com o Flask você pode escolher os componentes do seu aplicativo,ou até mesmo escrever o seu próprio, se assim o desejar. Sem perguntas! A chave para essa liberdade é que o Flask foi projetado desde o início para ser estendido.
Ele vem com um núcleo robusto que inclui a funcionalidade básica de que todos os aplicativos da
Web precisam e espera que o restante seja fornecido por algumas das muitas extensões de terceiros no ecossistema - e, é claro, por você.
Opencv Python é uma biblioteca de design de ligações Python para resolver problemas de visão computacional. É a API Python para Opencv. Ele foi construído para fornecer uma infraestrutura comum para aplicativos e para acelerar o uso da percepção da máquina. Suporta uma grande variedade de linguagens de programação como C++, JAVA etc e está disponível para diferentes plataformas para operações de alta velocidade. O Opencv Python faz uso do Numpy, que é uma biblioteca altamente otimizada para operações numéricas. É gratuito e pode ser escrito em qualquer idioma.
Suas áreas de aplicação incluem sistemas de reconhecimento, identificação de objetos,rastreamento, etc. Inclui uma biblioteca estatística de aprendizado de máquina que contém redes neurais, árvore de decisão e algoritmos de maximização.
