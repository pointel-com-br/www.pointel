# Desenvolvimento de Software - C# e Go

Índice

1) Desenvolvimento Back-End - C# - Teoria

2) Desenvolvimento Back-End - C# - Questões Comentadas.

3) Desenvolvimento Back-End - C# - Lista de Questões.

DESENVoLVIMENTo BACK-END - C#

WHY DO JAVA PROGRAMMERS
WEAR GLASSES?

THEY CAN'T SEE SHARP.

Olá! Antes de iniciarmos, é importante saber que nesta aula vou considerar que você já conhece o básico de lógica de programação, ok? Assim poderemos focar no que é específico deC#. Mas fique tranquilo, começaremos com os conceitos básicos, e nas resoluções das questões tudo está bem explicado, mas caso tenha alguma dúvida, fique mais do que à vontade para utilizar o fórum ou mandar um e-mail, ok?
Vamos começar pela sopa de letrinhas. C# é uma linguagem de programação.
.Net é um framework, que já possui uma biblioteca com várias soluções prontas. Visual Studio é aIDE, ou seja, é uma ferramenta que auxilia o desenvolvedor na criação dos sistemas,de forma mais produtiva. Agora sim, estamos prontos para entender mais sobre o desenvolvimento neste ambiente.
Um programa em C# é composto de três partes básicas, e hierárquicas: os Namespaces, as Classes e os Métodos.
/ 57

/

NAMESPACE

CLASSE
MÉTODO I

instrução instrução
MÉTODO 2

instrução instrução
Um programa está dentro de um
Namespace - ele indica que as classes pertencem à sua aplicação - para que o código fique separado do .Net Uma classe contém um "pedaço" do seu programa, deve haver no mínimo uma classe. Por sua vez, os métodos contém as instruções,que são ações individuais.

Um programa está dentro de um Namespace - ele indica que as classes pertencem à sua aplicação
- para que o código fique separado do .Net. Uma classe contém um "pedaço" do seu programa,deve haver no mínimo uma classe. Por sua vez, os métodos contêm as instruções, que são ações individuais.
Muito abstrato? Então vamos ver nosso primeiro trecho de código.

using System;

using System.Collections.Generic;
using System.Linq;

using System.Text;

namespace MinhaAplicacao {
class Program

{

static void Main(string[] args)

{

Console.Writel_ine("Oi! Eu sou o Goku.");

}

}

x' 4

/ 57

/

}

Então o que apareceu de diferente? Já sabemos que o .Net é um framework, ou seja,
nele estão contidas várias bibliotecas que podem ser utilizadas por sua aplicação. É exatamente isso que as primeiras 4 linhas do código acima estão fazendo, a palavra using é utilizada para incluir bibliotecas externas ao seu namespace.
Nessa aplicação temos apenas uma classe, Program, e um método, Main(). Todos os programasC# devem conter apenas um método Main(), ele é o ponto de entrada, é por ele que o programa inicia quando é executado.
Mas está muito simples não é? Vamos incluir uma nova variável.

namespace MinhaAplicacao {
class Program static void Main(string[] args)
{

string Nome = "Goku";
Console.Writel_ine("Oi! Eu sou o " + Nome);

}

Declaramos uma nova variável no formato:

Tipo nome_da_variavel [ = valorjnicial ];

O valorjnicial está entre colchetes pois é opcional. Simples não é? Essa é a estrutura básica de um programa C#! Agora vamos aprender mais alguns conceitos.
DESENVoLVIMENTo BACK-END - C#: ARRAYS

Em algum momento, você vai precisar trabalhar com vários dados do mesmo tipo,

e é para isso que servem os arrays, ou vetores. Para declarar é simples, defina o tipo seguido de colchetes:
int[] meuarray;
meuarray = new int[5];

Acabamos de criar um array, de inteiros e que foi inicializado com 10 números.
Perceba que é necessário utilizar o new pois arrays são objetos, eles precisam que seja alocada memória. Outra alternativa, é simplesmente, declarar e já iniciar, na mesma linha.
int[] meuarray = new int[5J;

Lembre-se o índice dos arrays começam no 0 (zero). Então para definir o valor da primeira variável temos que utilizar esta instrução: meuarray[0] = 55; Caso o array fosse de objetos,por exemplo,
Pessoa, cada índice guardaria um objeto, e precisaria ser inicializado: meuarray[0] = new PessoaO;

Mas se quisermos iniciar o array com 10 valores, não precisamos gastar 10 linhas para isso, basta declarar dessa forma:
stringf] Nomes = {"Ana", "Beto", "Carlos", "Daniel", "Elias", "Fernanda",
"Goku", "Hélio", "lan", "Jonas"};

/ 57

/

Console.Writel_ine("Oi! Eu sou o " + Nomes[6]);

//Você já sabe o que vai sair aqui, não é?

Você deve ter sentido falta de algo não é? Nesse caso não é obrigatório declarar com o "new string[10]", pois o compilador já aloca automaticamente o espaço necessário para os elementos que declaramos inicialmente.
DESENVoLVIMENTo BACK-END - C#: HERANçA

Herança é um conceito que está presente em toda a linguagem orientada a objetos, com
C# não é diferente. Quando você necessita que alguma classe tenha um comportamento mais específico,mas que ainda tenha o comportamento da classe mais geral, utilizamos a herança, ou seja uma classe estende a outra. Vamos pensar no clássico exemplo de animais. Se fossemos criar a superclasse Animal quais variáveis e métodos ela teria? Algo mais ou menos assim:
Esta é uma boa classe para representar todos os animais, eles todos fazem essas coisas. Porém nem todos fazem tudo igual, não é mesmo?
, 57

Agora, se fossemos criar as classes Hipopótamo e Cachorro quais métodos seriam diferentes? De acordo com a nossa tirinha (rs), Comer() seria um deles. Outro método diferente seria oFazerBarulhoO, o cachorro late e o hipopótamo grunhe (pesquisei essa). A subclasse modifica os métodos da superclasse (ou classe base) através da sobrescrita, em C# basta utilizar a palavra-chave override no método da subclasse, e a palavra-chave virtual no método da classe base.

Ao utilizar herança, a subclasse herda todos os atributos e métodos da classe base.
Mas caso você necessite que apenas alguns comportamentos sejam herdados, utilize a sobrescrita.
1. Adicione a palavra-chave virtual ao método na classe base. Só assim o C# vai saber que esse método poderá ser sobrescrito!
2. Adicione um método com a mesma assinatura na subclasse. A mesma assinatura é o mesmo nome, mesmo tipo de retorno e os mesmos parâmetros.
3. Adicione a palavra-chave override ao método da classe base.

Agora que já temos os conceitos básicos de herança, vamos ver um código de exemplo?

public class Animal {

//esta é nossa classe base: Animal.

public String nome;

//o atributo nome é público será herdado por todas as subclasses public virtual void FazerBarulho(){
/ 57

/

Console.Writel_ine(" Grunhido");

public virtual void Comer(){

Console.Writel_ine("Nhac");

/** os métodos FazerBarulhoO e Comer() estão marcados com a palavra-
chave virtual, ou seja podem ser sobrescritos. **/

public void Dormir(){

Console.Writel_ine("Zzz");

public void Andar(){

Console.Writel_ine(" Pegada");

}

/** já os métodos Dormir() e Andar() não poderão ser sobrescritos. Todos os animais que herdarem a classe Animal poderão Dormir e Andar apenas através desses métodos da classe base. **/
public class Cachorro : Animal {

/ 57

/

/** Cachorro será nossa primeira subclasse que extende Animal. Repare que o símbolo utilizado para indicar a herança é o sinal de dois pontos **/
public override void FazerBarulho(){
Console.Writel_ine("Au");

}

/** O método FazerBarulhoO foi sobrescrito, repare na palavra-chave override. Ela indica que o método que será chamado será o da classe filha,e não mais o da base. Ou seja, se você chamar cachorro.FazerBarulhoO. O
resultado será "Au" e não mais "Grunhido" **/

public override void Comer(){
Console.WriteLine("Hum... osso");

}

}

public class Hipopotamo : Animal {

public override void FazerBarulho(){
base. FazerBarulhoO;
Console. Writel_ine("?");

}

/ 57

/

/** O método FazerBarulhoO na classe Hipopótamo também foi sobrescrito, mas digamos que você não saiba o que o métodoFazerBarulhoO do Hipopótamo tem de diferente, você pode chamar novamente o FazerBarulhoO do Animal, é isso que a linha'base.FazerBarulhoO' faz, executa o método da classe base. Então o resultado desse método será "Grunhido?" **/
public override void ComerOf
Console.WriteLine("Hum... grama");

}

}

Código bem comentado não precisa de explicação certo? Esses são os conceitos básicos deHerança em C#.

DESENVoLVIMENTo BACK-END - C#: ENCAPSULAMENTo

Você deve ter percebido a palavra chave public em nossos exemplos de herança. Isso significa que todas as classes e métodos são visíveis por todas as outras classes da aplicação que as instanciarem.
TOME

NOTA!

X 57

/

Mas nem tudo deverá ser público não é mesmo? Para isso o C# possui modificadores de acesso,através deles é possível realizar o encapsulamento, ou seja, outras classes só verão o que for realmente necessário, a complexidade ficará "escondida". Caso nenhum modificador seja utilizado, o padrão para atributos e métodos é privado, e para classes e interfaces é internai.
bAoAiFicjiior Acesso public qualquer parte do programa que Faça reFerência a classe protectedinternai público apenas para classes no mesmo assembly e para subclasses internai público apenas para classes no mesmo assembly protected público para subclasses, privado para todo o resto private apenas na mesma classe
Um assembly é uma classe pré-compilada do framework .Net. Essas classes podem ser referenciadas por sua aplicação. Assemblies são implementados como arquivos .dll ou .exe que formam bibliotecas que podem ser utilizadas nos programas .Net.
DESENVoLVIMENTo BACK-END - C#: FoREACH

Um dos comando especiais do C# é o foreach, através dele é possível fazer um loop em qualquer lista genérica. Diferente do for que apenas itera até que uma condição seja verdadeira.
Mas o que é uma lista genérica? Elas também são chamadas de Collections. Um exemplo é a própria classe List (que faz parte do framework .Net), outro são os arrays. A questão é que para
/ 57

/

que possa ser percorrido pelo foreach obrigatoriamente sua coleção implementará a interfaceIEnumerable<T>.

Esclarecendo

Interfaces são os templates, ou seja, são "receitas" do que uma classe ter. Essa classe deverá implementar todos os métodos definidos na interface,
Uma classe que implementa a interface IEnumerable<T> permite que seus elementos sejam percorridos em ordem dentro de um, loop. Isso porque ela implementa o métodoGetEnumeratorO. 0 objeto retornado é o Enumerator. Este objeto é que permite ao

Foreach percorrer todos os elementos.

Vamos ver um trecho de código de exemplo?

List<Pessoa> pessoas = new List<Pessoa>();

[***]

foreach (Pessoa pessoa in pessoas)
{
Console. WriteLine(pessoa.name);

}

A saída desse loop serão os nomes de todas as pessoas que tiverem sido inseridas na lista, em ordem. Caso a lista esteja vazia, o loop não imprimirá nada.
Muito prático, não é mesmo? Mas como? O quê o foreach executa por trás das cortinas é isso:

X 57

/

IEnumerator<Pessoa> enumerator = pessoas.GetEnumeratorQ;

while (enumerator.MoveNextO) {
Pessoa pessoa = enumerator.Current;
Console. WriteLine(pessoa.name);

}

MoveNextO - retorna true se existe outro elemento na lista, e false quando o enumerator chega ao final da lista.
CurrentO - retorna uma referência para o elemento atual.

Muito mais fácil usar apenas o foreach não é mesmo? É importante lembrar dessa sintaxe! Olhe novamente o trecho de código acima e repare na colocação dos parentêses e da palavra reservada in.
DESENVoLVIMENTo BACK-END - C#: YIELD RETURN /
YIELD BREAK

Já entendemos como funciona a interface IEnumerable<T>, a partir do .Net 2.0 foi introduzida a instrução yield para auxiliar na criação de enumeradores para diferentes conjuntos de objetos,inclusive enums criadas pelo desenvolvedor. Vamos entender seu funcionamento através de exemplos.
Suponha que você quer retornar um conjunto de números de 1 a 100, provavelmente você faria algo parecido com o método abaixo:
public static List<int> GetListaNumerosQ

{

var lista = new List<int>();
for (int i = 0; i < 100; i++)

/ 57

/

{

lista.Add(i);

}

return lista;

}

Agora vamos ver o mesmo trecho utilizando o yield:

public static IEnumerable<int> GetListaNumerosO

{

for (int i = 0; i < 100; i++)

{

yield return i;

}

}

Vamos fazer o jogo dos 7 erros? Procure as diferenças!
Encontrou todas? Achou mais simples?

Logo de cara a gente percebe que não é preciso mais utilizar a lista genérica de inteiros. O que já nos poupou 2 linhas, além disso agora está mais claro que estou retornando números e não apenas uma variável chamada "lista".
Perceba que o retorno agora é IEnumerable<int>, ainda é uma lista! Essa é a "mágica"
do yield ele é um criador de objetos enumeráveis. Ou seja, você ainda irá retorna uma lista de 1até 100, a diferença é que a cada rodada do loop eu já retorno o objeto que está sendo inserido na lista.
Dessa forma há um ganho de desempenho, imagine se o loop não fosse só até 100, mas fossem milhões?
Yield return é um comando para a criação de objetos enumeráveis.

Como o retorno do nosso método GetListaNumerosO é um IEnumerable<int>, nós podemos utilizar este método dentro de um foreach.
foreach (int i in GetListaNumerosO)

{

Console.WriteLine("Meu número é: " + i);

}

Agora que já entendemos o yield return, ficou simples entender o yield break. Dentro de um loop normal o comando break sozinho faz a iteração parar certo? Com o yield break é a mesma coisa,a diferença é que ele vai mais além, ele encerra o método, ou seja, mesmo que esteja dentro de loops aninhados a execução vai terminar. Vamos para mais um exemplo:
public static IEnumerable<string> GetMaisResultadosO {
for (int i = 0; i < 20; i++) {

yield return "Valor " + i;
yield break;

}

//Faça outra coisa for (int i = 0; i < 20; i++) {
/ 57

/

yield return "Outro valor 11 + i;

}

}

Qual é o retorno desse método? Pense um pouquinho...

Se você falou "Valor 0" acertou! Se não, vamos entender agora? O yield break é poderoso lembra?Ele sai do método todo! E não apenas do loop. Então aquele segundo for depois do comentário"Faça outra coisa" não será executado.

DESENVoLVIMENTo BACK-END - C#: LINQ

LINQ é uma biblioteca introduzida no Visual Studio 2008. A sigla significa
Language Integrated
Query (Linguagem de Consultas Integrada), esta biblioteca ajuda o desenvolvedor a fazer consultas de dados uma maneira mais simples, agrupar dados, e também mesclar dados de diferentes fontes (coleções, banco de dados, até xml). Para utilizar o LINQ basta incluir no início do arquivo a linha using System.Linq.
/ 57

/

INDO

K_Zmais fundo

Vamos ver um trecho de código de exemplo da sintaxe do LINQ. Pegaremos um array e selecionaremos todos os numeros menores de 37 e colocaremos estes números em ordem crescente.Utilizaremos 4
cláusulas, que definirão qual é o objeto da consulta (from), qual critério será utilizado (where), como será feita a ordenação (orderby), e o quê será o retorno (retorno).
int[] valores = new int[] {0, 12, 44, 36, 92, 54, 13, 8};
var resultado from v in valores where v < 37orderby v selétt v; //no LINQ, diferentefnenite do SQL o seleet vem ao final,
foreach (int i in resultado)

Console.Write("{0} " , i};

Saída: 0 8 12 13 36

Obs: Repare que o resultado foi declarado como var, isso significa que em tempo de compilação o tipo será definido pelo .Net de acordo com o tipo da variável valores*
DESENVoLVIMENTo BACK-END - C#: *?' OPERADoR
CoNDICIoNAL T ERNÁRIo

O operador condicional '?' retornará um entre dois valores dependendo da condição. Esta é sua sintaxe: condicao ? primeira_expressao : segunda_expressao; Caso a condição seja verdadeira a primeira_expressao é retornada, caso seja falsa, a segunda_expressao é retornada. Vamos ver a comparação de um mesmo trecho de código feito com o if-else e com o '?'.
int string entrada Convert.Tolnt32(Console.Readl_ine());classificacao;

// construção com if-else.
/ 57

/

if (entrada >
classificacao =

else classificacao =
// ?: operador classificacao= (entrada > 0) ? "positivo" : "negativo";
0)

"positivo

"negativo condicional.
Curiosidade

O operador condicional é associativo à direita. A expressão a ? b : c ? d : e é desenvolvida como a ? b : (c ? d : e), não como (a ? b : c) ? d : e.
QUESTõES CoMENTADAS - DESENVoLVIMENTo BACK-END

- C# - MULTIBANCAS

1. (FGV - 2015 - Câmara Municipal de Caruaru - Analista Legislativo) Analise o código C# .NET a seguir.
for (int 1 = -5; i <= 7; i += 3)

{

Console.Writeline(i);

}

Assinale a opção que apresenta corretamente o resultado produzido pela execução do trecho acima.
a) 2,1,4, 7,10

b) 5, -2, 1, 4, 10

c) 2, 1,4,7

d) 5, -2, 1,4

e) 5,-2, 1,4, 7

Comentários:

Esse tipo de questão é muito comum, e você consegue resolver tranquilamente, basta realizar um teste de mesa, ou seja "rodar" o algoritmo, passo a passo.
Antes, vamos relembrar a sintaxe do for. Ele é um dos comandos de repetição, assim como o while. A variável i não precisa ter sido declarada anteriormente, você pode declará-la dentro do próprio for. Normalmente é um número inteiro int. As três instruções dos parênteses são as seguintes: (valor inicial; condição; incremento/decremento). Então nesse caso a variável i começa com -5.
O loop continuará até que i seja menor ou igual 7 (Isso é importante! Não erre e vá até o 6!). E a cada final de rodada o valor de i será somado a 3. Repare! Foi utilizado o operador+= que é a forma mais rápida de escrever i = i + 3.
A instrução de dentro do for, Console.WriteLine(i); Apenas escreve o valor da variável na saída e pula uma linha. A saída pode ser o terminal, mas se você estiver utilizando o VisualStudio, sairá na aba Output.
Agora ficou fácil não é? Vamos ao teste de mesa:

/ 57

/

1o passo) i = -5, i <= 7, saída: -5, i = -5 + 3

2o passo) i = -2, i <= 7, saída: -2, i = -2 + 3

3o passo) i = 1, i <= 7, saída: 1, i = 1 +3

4o passo) i = 4, i <= 7, saída: 4, i = 4 + 3

5o passo) i = 7, i <= 7, saída: 7, i = 7 + 3

6o passo) i = 10, i > 7, condição retorna false, não entra mais no loop. Gabarito: E

2. (FGV - 2015 - TCE/SE - Analista de Sistemas) Analise o código C# mostrado abaixo.

namespace ConsoleApplicationl

{

class Program

{

static IEnumerable<int>
XPT0(int from, int to) {

for (int i = from; i < to; i+=3) {
yield return i;

}

yield break;

}

static void Main()

{

foreach (int x in XPTO(-10, 10) {
Console.WriteLine(x);

}

O resultado exibido pelo programa é:

a) -10

b) -10, -7, -4, -1, 2, 5, 8 <-

c) -7,-4, -1,2, 5,8

d) -7,-4,-1,2, 5,8,11

e) 0

Comentários:

Vamos iniciar a execução desse programa pelo método MainO, dentro dele temos um foreach chamando o método XPTO com os argumentos -10 e 10. Esses argumentos são os parâmetros
X 57

/

from e to. Eles são os valores de início (from) e fim (to) do for que está dentro do método. Então,vamos traduzir o for:

for (int i = -10, i < 10;i += 3) {
yield return i;

}

yield break;

Nessa aula já vimos o funcionamento do yield return e do yield break. Então repare que o yield break está fora do for, isso significa que o loop será executado até o final preenchendo a listaIEnumerable<int>. Então os valores retornados irão começar de -10, pulando de 3 em 3,
até o último número menor que 10: -10, -7, -4, -1, 2, 5, 8 (8+3 é 11. Ultrapassa 10 e não entra.).Retornamos então para o método Main(), o foreach apenas percorre todos os valores e eles são escritos na tela. Gabarito: B
3. (FGV - 2015 - TJ/BA - Analista Judiciário) Observe o trecho inicial, criado no Visual Studio
2010
Ultimate, para uma aplicação de console escrita em C#.

using System;

using System.Collections.Generic;
using System.Linq;

using System.Text;

namespace ConsoleApplicationl {
class Program

{

static void Main(string[] args)

{

}

}

}

A diretiva using System.Linq refere-se a um conjunto de padrões e artefatos destinados à:

a) criação e utilização de relatórios;

b) realização de consultas e atualizações de dados;

c) criação e utilização de expressões regulares;

d) comunicação remota direta com outras aplicações C#;

/ 57

/

e) identificação e utilização de Web Services.

Comentários:

Como visto na aula, o namespace System.Linq fornece classes e interfaces que suportam consultas que utilizam a Language-lntegrated Query (LINQ) para consulta e atualização de dados.Gabarito:
B

4. (FGV - 2014 - DPE-RJ - TÉCNICO SUPERIOR ESPECIALIZADO -
ANALISTA DE
DESENVOLVIMENTO DE SISTEMAS)

Considere o código escrito na linguagem C# mostrado a seguir.

u s ing S y stem.IO;
using System;

public class Veiculo

{ public virtual void mover {)

( Console .Write ("Movendo") ;

}

public class Automovel:Veiculo

{ public override void mover()

( Console.Write("Acelerando");

}

public class Fusca: Automovel

{ public override void mover{)

( Console.Write ("Passeando");

}

class Program

{ static void Main()

( Veiculo veiculo = new Fusca();
veiculo.mover();

}

}

O resultado produzido pela execução desse código é:

a) Acelerando.

b) Passeando.

c) Movendo.

d) MovendoAcelerandoPasseando.

e) AcelerandoPasseando.

Comentários:

/ 57

/

Essa é uma questão simples, mas que pode assustar. Mas não você! Nós já sabemos como funciona a herança. A hierarquia no código dessa questão (do mais especializado para o mais generalizado)é Fusca -> Veículo -> Automóvel. Todos possuem o método mover(). Mas você deve ter reparado que Automóvel e Fusca utilizaram a palavra chave override. Ou seja, estão sobreescrevendo o método da classe pai.
Agora vamos analisar o método Main(). Perceba que apesar do tipo ser do pai, Veículo,
o objeto criado foi o Fusca. Ou seja, a variável veiculo referencia um objeto Fusca. Não é errado tipar um objeto da classe mais especializada (subclasse - filho) com o tipo da classe mais generalizada(classe base - pai). Afinal podemos chamar um Fusca de Veículo na vida real não é mesmo?

Então agora você já sabe o que acontecerá quando o métoodo executar veiculo.mover(). Será chamado o método mover() da classe Fusca. Esse método simplesmente escreve "Passeando"na tela. Gabarito: B
5. (FGV - 2014 - DPE/RJ - Técnico Superior Especializado - Analista De
Desenvolvimento De
Sistemas)

Na linguagem C#, a forma correta para inicializar um array de inteiros de cinco posições, com os números de 1 até 5 é:
a) int[] lnteiros={1,2,3,4,5};

b) int[] lnteiros=[1,2,3,4,5J;

c) int[5] lnteiros={1,2,3,4,5};

d) int lnteiros[]={1,2,3,4,5};

e) int lnteiros[]=new int[5]{1,2,3,4,5};

Comentários:

Lembre-se a sintaxe de declaração do C# segue o formato Tipo nome_da_variavel =
inicializacao.
Para arrays o tipo deve ser seguido por colchetes vazios: int[]. E caso deseje inicializar com valores não é obrigatório o uso do new, basta colocar os valores entre chaves: int[] inteiros= {1,2,3,4,5}.
O item B usa colchetes no lugar das chaves, o item C coloca a quantidade de elementos dentro dos colchetes do tipo, o item D coloca os colchetes após o nome da variável, e a letra E contém o mesmo erro da letra D (a inicialização com new apesar de desnecessária, pois o compilador já sabe que precisa alocar um espaço de 5 inteiros na memória, não está errada). Gabarito: A
6. (VUNESP - 2014 - TCE/SP - Agente Da Fiscalização Financeira) Observe a declaração de um vetor em C#:
int[] vetor = new int[3] {1, 2, 3 };

Sem alterar o resultado, essa mesma declaração poderia ser escrita como:

a) int[] vetor = { 1, 2, 3 };

b) int[] vetor = int { 1, 2, 3 };

c) int[] vetor = new { 1, 2, 3 };

d) int[] vetor = new int[];

e) int[] vetor = new int[] = { 1, 2, 3 };

Comentários:

Essa está tranquila, as letras b), c), d) e e) darão erro de compilação, não existe essa sintaxe. Aletra a) é a correta, inclusive é até mais correta do que o enunciado, pois é desnecessária a inicialização utilizando new quando já colocamos os valores desejados para o vetor entre colchetes. Gabarito: A
7. (VUNESP - 2014 - PRODEST/ES - Analista De Tecnologia Da Informação) Na linguagem de programação C#, a sintaxe correta para declarar um objeto do tipo Carro e produzir uma nova instância desse objeto é:
a) Carro obj = new Carro();

b) Carro obj = Carro.new;

c) Carro obj = Carro();

d) Carro = new Carro();

e) obj = CarroQ;

Comentários:

Simples não é? Você já sabe que a sintaxe de declaração do C# é TipoObjeto nome_da_variavel
= new TipoObjetoQ; Gabarito: A

8. (VUNESP - 2014 - PRODEST/ES - Analista De Tecnologia Da Informação) Na linguagem de programação C#, a declaração dos tipos e de seus membros permite que seja determinada a sua visibilidade por meio de modificadores de acesso. Os modificadores disponíveis para esse fim são:
a) default, open, closed, partial e full.

b) full-access, write, write-only, read e read-only.

c) global, local, nested e virtual.

X 57

/

d) public, private, published e protected.

e) public, private, protected, internai e protected internai.

Comentários:

Conforme vimos na aula, C# possui 5 modificadores de acesso. Você já sabe quais são não é?
Gabarito: E

9. (VUNESP - 2013 - IMESC - Analista De Tecnologia) Na linguagem C#, para inserir um elemento no final de um ArrayList, deve ser utilizado o método:
a) Add.

b) AddToEnd.

c) Append.

d) Insert.

e) Put.

Comentários:

Um ArrayList é um tipo do .Net que pode ser utilizado ao adicionar using
System.Collections. É
uma lista de objetos não genérica. Para adicionar um elemento ao final do array utilizamos o método Add(object value). E o elemento sempre será inserido ao final do ArrayList. Oúnico outro método que existe é o lnsert(int index, object value). Nesse caso, o objeto será inserido no índice especificado como parâmetro. Gabarito: A
10. (VUNESP - 2013 - IMESC - Analista De Tecnologia) Analise o seguinte trecho de código em linguagem C#:
int x = 10;
int y = 20;

x. += x. == 20 ? x / y : y / x;
y -= y == 10 ? y / x : x / y;

Após a execução desse trecho de código, o valor das variáveis "x" e "y" serão, respectivamente,

a) 2 e 0.

b) 10 e 18.

c) 10 e 20.

X 57

/

d) 12 e 19.

e) 12e20.

Comentários:

Nessa questão vamos trabalhar com o operador condicional ternário '?'. Como já foi abordado na aula fica fácil, vamos executar o algoritmo?
A primeira coisa que devemos fazer é separar as expressões a maior hierarquia é a atribuição,então podemos simplificar para x += expressaol e y += expressao2; Agora é só resolver as expressões 1 e 2.
expressaol: x == 20 ? x/y : y/x;

Nossa condição é x == 20? 10 == 20? Falso. É retornada a segunda expressão: y/x= 20/10 = 2.
Então, expressaol = 2. E x += 2 é o mesmo que x = x + 2 => x = 12.

expressao2: y == 10 ? y/x : x/y;

Nossa condição é y == 10? 20 == 10? falso. É retornada a segunda expressão: x/y=
10/20 = 0
(lembre-se que estamos trabalhando com inteiros!).

Então, expressao2 = 0ey-=0éo mesmo que y = y - 0 => y = 20. Gabarito: E

11. (VUNESP - 2013 - MPE/ES - Agente Técnico - Desenvolvedor) Na linguagem C#, é possível dividir a definição de uma classe em diversos arquivos. Para tanto, é necessário que a declaração da classe contenha a palavra chave:
a) split b) parti a I
c) extern d) continue e) abstract
Comentários:

Apesar de não ter abordado na aula podemos trabalhar por eliminação. Sabemos que
'abstract' é a classe que não pode ser instanciada, que precisa ser implementada por outra classe,'continue'
é a palavra chave utilizada em loops quando você quer que a iteração continue e que o restante das instruções sejam "puladas", o 'extern' é um modificador que indica que seu método é implementado fora da sua classe. Aí nos sobram split e partial, as duas palavras caberiam, mas se você lembrar que split é na verdade um método para separar strings, sobra apenas o partial
X 57

/

Uma classe pode ser dividida em vários arquivos, quando o compilador vê a palavra-chave partial ele sabe que este arquivo é apenas um pedaço da classe. Um exemplo de uso dessas classes parciais são os formulários do Visual Studio, se você adicionar um form em seu projeto, a IDE irá criar dois arquivos, um com a parte do formulário que você pode alterar e outro com o código que é gerado automaticamente. Gabarito: B
12. (VUNESP - 2013 - MPE/ES - Agente Técnico - Desenvolvedor) Na linguagem C#, a forma correta de declarar a classe B, derivada da classe A, é:
a) public class B inherits A {}

b) public class B => A {}

c) public class A extends B {}

d) public class B : A {}

e) public class B implements A {}

Comentários:

Essa você já sabe não é? Vimos na aula. Em C# a sintaxe é a mesma tanto para herança quanto para a implementação de interfaces. Gabarito: D
13. (VUNESP - 2013 - MPE/ES - Agente Técnico - Desenvolvedor) Na linguagem C#, a palavra reservada "sealed" pode ser utilizada na declaração de classes. Ela tem a função de a) indicar que a classe possui métodos que precisam ser sobrescritos.
b) impedir que a classe seja instanciada mais de uma vez.

c) impedir que a classe seja derivada por outras classes.

d) garantir que a classe não seja instanciada por classes que não estejam no mesmo namespace.

e) indicar que o conteúdo da classe é imutável, isto é, uma vez instanciada, seu conteúdo não é mais alterado.
Comentários:

Esse é um modificador extra da linguagem C# e indica que a classe não pode ser derivada, ou seja, não há herança, ela está "selada", "fechada". Gabarito: C
14. (AOCP - 2012 - TCE/PA - Assessor Técnico - Analista De Sistemas) Em C#, os métodos chamados pelo mecanismo de execução do programa quando o objeto está prestes a ser removido da memória são denominados de:
X 57

/

a) Garbage Collection.

b) Destruidores.

c) Propriedades.

d) Indexadores.

e) Eventos.

Comentários:

As alternativas deixaram a questão fácil, mas vamos aproveitar e falar um pouquinho dos destrutores ou destruidores. Como o enunciado diz, os destruidores não podem ser chamados explicitamente, quem os chama é o Garbage Collector (Coletor de Lixo). Abaixo um exemplo de destruidor, ele é definido pelo sinal seguido pelo nome da classe.
class
Exemplo

{

-ExemploO

{

System.Diagnostics.Trace.WriteLine("O destruidor da Classe Exemplo foi chamado.");
}

}

Gabarito: B

15.(AOCP - 2012 -TCE/PA - Assessor Técnico - Analista De Sistemas) Analise o seguinte trecho do código C#:
(. . .)

01 double x = 1432.7;

02 int y;

03 y = (int)x;
(-)

Sobre a linha 03 do código apresentado, é correto afirmar que:

a) a variável y recebe o valor de x se esta última (x) for do tipo int.

b) atribui à variável y o valor da variável x convertido para o tipo int.

c) passa como parâmetro o valor da variável x para y, do tipo double.

d) a variável y recebe por referência o valor da variável x do tipo double.

x'"'

/ 57

/

e) multiplica o valor da variável int por x e atribui o valor calculado para a variável y.

Comentários:

Este é um exemplo do cast que é a conversão pelo compilador de uma variável de um tipo para outro tipo. Várias linguagens fazem o cast. Não é diferente em C#. Gabarito: B
16. (AOCP - 2012 - TCE/PA - Assessor Técnico - Analista De Sistemas) Segundo a Microsoft, um conjunto de recursos introduzidos no Visual Studio 2010 que estende as capacidades de consultas à sintaxe da linguagem de C# e Visual Basic é conhecido como:
a) LINQ.

b) T-SQL.

c) OQL.

d) ADO.

e) ASP.

Comentários:

Cabe recurso, pois o LINQ foi introduzido no Visual Studio 2008. Mas realmente os recursos da biblioteca LINQ trazem novas capacidades para que o desenvolvedor trabalhe com consultas.Gabarito: A

17. (AOCP - 2012 - TCE/PA - Assessor Técnico - Administrador De Banco De Dados)
Sobre a linguagem C# assinale a alternativa correta.
a) É uma linguagem de programação orientada a objetos, desenvolvida pela Microsoft como parte da plataforma .NET caracterizada por ser fracamente tipada.
b) É a única linguagem de programação que suporta herança múltipla pura, ou seja,
cada classe pode herdar características de uma ou mais classes.
c) A linguagem não suporta ponteiros porque os blocos de códigos requisitariam permissões mais altas de segurança para serem executados.
d) O garbage collection é um processo usado para a manutenção do processador evitando erros comuns que podem levar ao encerramento do programa.
e) Há três tipos de passagem de parâmetros, por valor, por referência e por saída.

Comentários:

/ 57

/

(a) É uma linguagem fortemente tipada; (b) Não suporta herança múltipla; (c)
Ponteiros são suportados (int* p - p é um ponteiro para um inteiro); (d) O garbage collection é o processo de"coleta de lixo", através dele objetos que não são mais referenciados podem ser liberados da memória, que fica livre para a utilização por outro objeto. Gabarito: E
18. (FCC - 2014 - TRF3 - Analista Judiciário - Informática)

X 57

/

Utilize o programa C# abaixo para responder as questões de números 43 e 44.

Os números à esquerda não fazem parte do programa, apenas indicam os números das linhas.

[1] using

[2] using

[3] using

[4] using

System;
System.Collections.Generic;
System.Linq;

System.Text;

[5] namespace ConsoleApplicationl

[6] {

[7] public static class ConverteTemp

[8] {

[9] public static double CelsiusToFahrenheit(string tempCelsius)

[10] {

[11] double celsius = Double.Parse(tempCelsius);

[12] double fahrenheit = (celsius *9/5) +32;

[13] return fahrenheit;

[14] }

[15] public static double FahrenheitToCelsius(string tempFahrenheit)

[16] {

[17] double fahrenheit = Double.Parse(tempFahrenheit);

[18] double celsius = (fahrenheit - 32) *5/9;

[19] return celsius;

[20] }

[21]

[22] }

[23] class TestaConverteTemp

[24] {

[25] static void MainO

[26] {

[27] Console.WriteLine("Selecione a conversão desejada");

[28] Console.WriteLine("1. De Celsius para Fahrenheit.");

[29] Console.WriteLine("2. De Fahrenheit para Celsius.");

[30] Console.Write(":");

[31] string opcao = Console.ReadLine();

[32] double F, C = 0;

[33] switch (opcao)

[34] { case "1": Console.Write("Digite a temperatura em Celsius: ");

[35] F = ConverteTemp.CelsiusToFahrenheit(Console.ReadLine());

[36] Console.WriteLine("Temperatura em Fahrenheit: {0:F2}"> F)

[37] break;

[38] case "2": Console.Write("Digite a temperatura em Fahrenheit: ");

[39] C = ConverteTemp.FahrenheitToCelsius(Console.ReadLine());

[40] Console.WriteLine("Temperatura em Celsius: {0:F2}", C);

[41] break;

[42] default: Console.WriteLine("Opcao invalida.");

[43] break;

[44] }

[45] Console.WriteLine("Pressione uma tecla para finalizar.");

[46] Console.ReadKey();

[47] )

[48] }

[49] }

O programa C# apresentado é executado apenas uma vez e finaliza. Para que o programa possa ser executado diversas vezes, até que o usuário digite 0 para finalizá-lo é necessário inserirConsole.Writel_ine("0. Finaliza."); como mais uma opção do menu e inserir a seguinte instrução de repetição:
a) while (opcao != 0) antes do switch, que está na linha 33, com os delimitadores de início e fim {} desta instrução envolvendo as linhas 33 a 44.
b) while (opcao != "0") antes do switch, que está na linha 33, com os delimitadores de início e fim {} da instrução envolvendo as linhas 33 a 44.
c) for (; ;) { após o delimitador de início de bloco { na linha 26 e uma chave }
para fechar o bloco logo após a linha 44. Antes do switch, que está na linha 33, inserir o comando if (opcao
== "0") break;

d) do antes do switch, que está na linha 33, com o delimitador de início { da instrução envolvendo as linhas 33 a 44, e finalizando com o delimitador de fim } while (opcao != "0");
e) for (opcao=0;opcao<3;opcao++) após o delimitador de início de bloco { na linha 26
com os delimitadores de início e fim {} da instrução envolvendo as linhas 27 a 44.
Comentários:

(a) Dentro do while, a condição está errado pois 0 é do tipo int e opção é do tipo string isso causará um erro de compilação; (b) Caso o while termine na linha 44, o valor da variável opção nunca será atualizado, então caso o usuário selecione a opção = "1", o programa entrará em um loop infinito,sempre executando o trecho dentro do switch case opcao = "1";

(c) Perfeito. Ao colocar o loop for na linha 26, o usuário visualizará novamente o menu e poderá executar o programa quantas vezes desejar. Já que o for não possui condições. Porém,ao colocar o comando 'if (opcao == "0") break;' o loop é interrompido quando o usuário selecionar a opção"0";d) Aqui temos o mesmo problema da letra B;

(e) Mesmo erro da letra B. E além disso, nesse caso não adianta trabalharmos com o valor de opcao no for, pois ele será sobrescrito pelo valor que o usuário digitar. Então mesmo que o usuário digite a opção 0, não sairá do programa pois a condição continua sendo válida opção é < 3.Gabarito: C

19.(FCC - 2014 - TRF3 - Analista de Sistemas) Considerando o programa e a linguagem
C#, é correto afirmar:
a) Console é uma classe. As classes Object e System herdam desta classe.

b) Na linha [25]: Quando o aplicativo é iniciado, o método Main é o primeiro método invocado.Em C#, bibliotecas e serviços não requerem um método Main como um ponto de entrada.

c) WriteLine é um método da classe Console. Como a classe System herda da classe
Console,
então WriteLine também é um método da classe System.

/ 57

/

d) Na linha [11 ]: double celsius = Double.Parse(tempCelsius); significa que double é uma classe e Parse é um método desta classe.
e) Na linha [42]: default é um atributo exclusivo do comando switch e é usado apenas quando um valor numérico que não conste dos cases é fornecido pelo usuário.
Comentários:

(a) Console é sm uma classe, ela representada a entrada e saída padrão para a aplicações de console. Porém System é o namespace para as classes bases do .Net. A classe Console e a classeObject estão dentro deste namespace; (b) Certo; (c) A classe Console não pode sofrer herança.Ela faz parte do namespace System; (d) Double com letra maiúscula é uma classe, que contém métodos como o Parse(). Já double, com letra minúscula, é um tipo primitivo; (e) Dois erros. Os valores não são numéricos, são strings. E o atributo default também é utilizado fora do switch para indicar qual é o valor default de um tipo parametrizado (Este é um conceito avançado que não cabe em nossa aula, caso queira saber mais veja a referência oficial). Gabarito: B
20. (CESPE - 2013 - BACEN - Analista De Sistemas)

class Teste f static void Main()
f int num = 1;
while (num++ < 6)

f

Console.WriteLine ("num é = {0}", num);

}

}

}

Nessa situação, essa classe produz o seguinte resultado:

a) num é = 1

b) num é = 2

c) num é = 3

d) num é = 4

e) num é = 5

/ 57

/

Comentários:

Repare que no while a variável num já é incrementada (num++). Então a primeira linha a ser escrita é "num é = 2). Outra curiosidade dessa questão é a utilização de um parâmetro. Ovalor entre chaves {0} será substituído pelo valor do argumento que vem logo em seguida. Gabarito: ERRADO
21.(CESPE - 2013 - BACEN - Analista De Sistemas) Em C#, o operador ?? é denominado operador de concentração de nulo e é usado para definir um valor padrão para tipos de valor anulável ou tipos de referência. No exemplo abaixo, caso a variável num seja nula, o valor de x será igual a
1. int x = num ?? 1;

Comentários:

Exatamente, este operador equivale a if (x == null) return 1; Gabarito: CERTO

22.(CESGRANRIO - 2013 - IBGE - Analista De Sistemas) O que ocorre com o programa C#,
apresentado abaixo, quando é compilado e posteriormente executado?

using System;
public claaa Prova

{

puhlic static void Main()

{

int[] a=new int[10];
int i=D;

while (i<10) {

a[i] = i + (i>0 ? a[i-l] : 0) ;
i++ '

}

Console.WriteLine(a[9]);

a) Compila corretamente, executa e imprime o número 45.

b) Compila corretamente, executa e imprime o número 9.

c) Compila corretamente e executa, mas nunca termina.

d) Compila corretamente, mas apresenta erro de execução.

e) Apresenta erro na compilação.

/ 57

/

Comentários:

Esta é uma ótima questão para relembrarmos o funcionamento dos arrays e do operador condicional ternário.
Primeiramente é declarado um array 'a' de inteiros, com 10 posições;

Em seguida é declarada a variável auxiliar 'i' também inteiro e inicializada com o valor 0 (Lembre-se que o primeiro índice dos vetores é 0 e não 1, então o vetor de tamanho dez irá de a[0] até o a[9]). O loop while irá preencher o vetor 'a'.
A expressão do ternário é a seguinte: i > 0 ? a[i-1 ]: 0.

Então na primeira iteração, o resultado é falso, será retornado o valor da segunda expressão 0.a[0] = 0 + 0 => 0.

Nas próximas iterações, a condição do ternário será verdadeira (i>0), o vetor receberá o valor do índice siornado ao Vc ilor guardado na posição anterior a[i-1 ].
a[1] = 1 + a[0] = 1 + 0 => 1.

a[2] = 2 + a[1] = 2 + 1 => 3.

a[3] = 3 + a[2] = 3 + 3 => 6.

a[4] = 4 + a[3] = 4 + 6 => 10.

a[5] = 5 + a[4] = 5 + 10 => 15.

a[6] = 6 + a[5] = 6 + 15 => 21.

a[7] = 7 + a[6] = 7 + 21 => 28.

a[8] = 8 + a[7] = 8 + 28 => 36.

a[9] = 9 + a[8] = 9 + 36 => 45.

O array está completo, e o loop while chega ao fim (i=10). E o valor impresso será o valor de a[9]
= 45. Gabarito: A

23.(CESGRANRIO - 2012 - EPE - Analista De Gestão Corporativa - Tecnologia Da Informação) Na programação orientada a objeto, na linguagem C# em particular, a capacidade de construir vários métodos com um mesmo nome, porém com parâmetros diferentes na mesma classe, é chamada de a) Polimorfismo universal b) Polimorfismo paramétrico c) Polimorfismo de subtipo d) Sobrecarga de operadores
, 57

e) Sobrecarga de métodos

Comentários:

Esta é a descrição da sobrecarga (overload). Lembre-se: se a assinatura é diferente é sobrecarga,se a assinatura for igual é sobrescrita (override). Gabarito: E

24. (CESGRANRIO - 2010 - ELETROBRAS - Analista De Sistemas - Engenharia De Software)
O
programador de um sistema Web deseja imprimir, em determinada tela, a hora atual. Que fragmento de código C# atinge esse objetivo?
a) Now.ToStringO;

b) DateTime.Now.ToString( HH:mm );

c) DateTime.Actual.ToString( HH:mm );

d) Time.Now.ToString( HH:mm );

e) Now.ToString( HH:mm );

Comentários:

Esse é aquele tipo de questão que a gente tem que ter visto antes para acertar. A
struct que possui as informações de Data é a DateTime e o atributo Now retorna a hora, dia, mes e ano atuais de acordo com o sistema. O método ToString formata o resultado para mostrar as horas e minutos(HH:mm). O m minúsculo é para não confundir com M maísculo do Mês. Gabarito: B

25. (CESGRANRIO - 2010 - EPE - Analista De Gestão Corporativa - Tecnologia Da
Informação)
Determinado órgão público federal deseja implantar um sistema de consulta na Internet. A
plataforma utilizada será ASP.NET e a linguagem de programação, C#. Na modelagem orientada a objetos desse sistema, é importante considerar que a linguagem adotada:
a) impede, no contexto de instanciação de objetos, o uso de classes abstratas.

b) impede somente o uso de polimorfismo a fim de assegurar a legibilidade do código.

c) apresenta o conceito de namespaces para implementar associações entre classes.

d) proíbe o uso de interfaces para garantir a coesão e a modularidade do código.

e) implementa, no âmbito da generalização, somente herança simples.

Comentários:

Apesar de comentar sobre a plataform ASP.NET a questão é sobre C#. Já vimos na aula que C#possui classes abstratas, polimorfismo (através de sobrecarga e sobreescrita), interfaces e que os
/ 57

/

namespaces servem para organizar as classes de uma biblioteca, e não associá-las. E
também vimos que é implementada a herança simples. Gabarito: E
26.(FGV - 2016 - IBGE- Análise De Sistemas - Desenvolvimento De Sistemas) Analise o código C#
exibido a seguir:

using System;
namespace ENIGMA

{

class Program {

static void Main(string[] args) {
P d = new P();

d.PPO;

E s = new E();
s.A0;

s.PPO;

Console.ReadKeyO;

}

class P {

public void PPO

{

Console.WriteLine("PP");

}

}

class E : P {
public void A()

{

Console.Writel_ine("A");

}

}

}

}

O resultado produzido no console é:

a) PP
A
PP

b) PP
PP

c) A

PP
A

d) AA

P
AA

e) A

A
A

Comentários:

Questão de lógica de programação. Nesse programa temos a classe P que tem o método
PP() e a classe E que herda de PP() - lembre-se que o operador (dois pontos) significa herança. Então começamos a executar pelo Main.
Primeiro, é criado o objeto d do tipo P, ao chamar o método PP(), já é escrito na saída "PP", em seguida é criado o objeto s do tipo E. Ele chama o método A(), que escreve no console "A" depois ele chama o método PP(), ele pode pois E herda de P, e escreve no console "PP"novamente.
Então a saída fica PP/ A/ PP. Como writeline pula linha, e readkey mantém o cursos no mesmo ponto, letra A. Gabarito: A
27. (FGV - 2016 - IBGE - Análise De Sistemas - Desenvolvimento De Sistemas)
using System;

namespace TESTE

{

class Program

{

delegate int del(int i);

static void Main(string[] args)

{

dei myF = x => x * x;
int j = myF(5); //j = 25

Console.WriteLine(j.ToString());

}

}

}

O resultado produzido no console é:

a) 5

b) 25

c) False d) True e) x * x
Comentários:

Vamos analisar o código, tem um elemento diferente os delegates eles são nada mais que ponteiros para função, porém já tem tipo de retorno e de parâmetro definido. Ou seja, foi declarado um delegado para uma função chamada dei que recebe um parâmetro inteiro e retorna um inteiro. No Main() o método myF foi atribuído ao dei. A sintaxe é (parâmetro) =>(corpo do método). Então para myF o parâmetro é x e no corpo do método acontecerá x*x. Ou seja, o método myF receberá um número e receberá sua primeira potência. No exemplo ele atribuiu ao int j, myF(5), ou seja 5*5 = 25. Engraçado que ele até coloca um comentário com a resposta j =
25. Ao final ele apenas escreve o valor de j, transformado em string. Ou seja, 25. Gabarito: B

, 57

LISTA DE QUESTõES - DESENVoLVIMENTo BACK-END - C#

- MULTIBANCAS

1. (FGV - 2015 - Câmara Municipal de Caruaru - Analista Legislativo) Analise o código C# .NET a seguir.
for (int 1 = -5; i <= 7; i += 3)

{

Console.Writeline(i);

}

Assinale a opção que apresenta corretamente o resultado produzido pela execução do trecho acima.
a) 2, 1, 4, 7, 10

b) 5,-2, 1, 4, 10

c) 2, 1,4,7

d) 5,-2, 1,4

e) 5,-2, 1,4, 7

2. (FGV - 2015 - TCE/SE - Analista de Sistemas) Analise o código C# mostrado abaixo.

X 57

/

namespace ConsoleApplicationl

{

class Program

{

static IEnumerable<int>
XPTO(int from, int to) {

for (int i = from; i < to; i+=3) {
yield return i;

}

yield break;

}

static void Main()

{

foreach (int x in XPTO(-10, 10) {
Console.WriteLine(x);

}

O resultado exibido pelo programa é:

a) -10

b) -10, -7, -4, -1, 2, 5, 8 <-

c) -7,-4, -1,2, 5,8

d) -7,-4,-1,2, 5,8,11

e) 0

3. (FGV - 2015 -TJ/BA-Analista Judiciário) Observe o trecho inicial, criado no Visual Studio 2010
Ultimate, para uma aplicação de console escrita em C#.

using System;

using System.Collections.Generic;
using System.Linq;

using System.Text;

namespace ConsoleApplicationl {
class Program

{

static void Main(string[] args)

{

}

A diretiva using System.Linq refere-se a um conjunto de padrões e artefatos destinados à:

a) criação e utilização de relatórios;

b) realização de consultas e atualizações de dados;

c) criação e utilização de expressões regulares;

d) comunicação remota direta com outras aplicações C#;

e) identificação e utilização de Web Services.

4. (FGV - 2014 - DPE-RJ - TÉCNICO SUPERIOR ESPECIALIZADO - ANALISTA DE
DESENVOLVIMENTO DE SISTEMAS)

Considere o código escrito na linguagem C# mostrado a seguir.

using S y st em.IO;
using System;

públic class Veiculo

{ públic virtual void mover()
( Console.Write("Movendo") ;

}

públic class Automovel:Veiculo

{ públic override void mover ()

( Console.Write{"Acelerando") ;

}

públic class Fusca:Automóvel

{ públic override void mover{)

( Console.Write ("Passeando");

}

class Program

{ static void Main()

( Veiculo veiculo = new Fusca();
veiculo.mover();

}

}

O resultado produzido pela execução desse código é:

a) Acelerando.

b) Passeando.

c) Movendo.

d) MovendoAcelerandoPasseando.

e) AcelerandoPasseando.

5. (FGV - 2014 - DPE/RJ - Técnico Superior Especializado - Analista De
Desenvolvimento De
Sistemas)

Na linguagem C#, a forma correta para inicializar um array de inteiros de cinco posições, com os números de 1 até 5 é:
a) int[] lnteiros={1,2,3,4,5};

b) int[] lnteiros=[1,2,3,4,5J;

c) int[5] lnteiros={1,2,3,4,5};

d) int lnteiros[]={1,2,3,4,5};

e) int lnteiros[]=new int[5]{1,2,3,4,5};

6. (VUNESP - 2014 - TCE/SP - Agente Da Fiscalização Financeira) Observe a declaração de um vetor em C#:
int[] vetor = new int[3] {1, 2, 3};

Sem alterar o resultado, essa mesma declaração poderia ser escrita como:

a) int[] vetor = { 1, 2, 3 };

b) int[] vetor = int { 1, 2, 3 };

c) int[] vetor = new { 1,2, 3 };

d) int[] vetor = new int[];

e) int[] vetor = new int[] = { 1, 2, 3 };

7. (VUNESP - 2014 - PRODEST/ES - Analista De Tecnologia Da Informação) Na linguagem de programação C#, a sintaxe correta para declarar um objeto do tipo Carro e produzir uma nova instância desse objeto é:
a) Carro obj = new CarroO;

b) Carro obj = Carro.new;

c) Carro obj = CarroO;

d) Carro = new CarroO;

, <

X 57

/

e) obj = CarroQ;

8. (VUNESP - 2014 - PRODEST/ES - Analista De Tecnologia Da Informação) Na linguagem de programação C#, a declaração dos tipos e de seus membros permite que seja determinada a sua visibilidade por meio de modificadores de acesso. Os modificadores disponíveis para esse fim são:
a) default, open, closed, partial e full.

b) full-access, write, write-only, read e read-only.

c) global, local, nested e virtual.

d) public, private, published e protected.

e) public, private, protected, internai e protected internai.

9. (VUNESP - 2013 - IMESC - Analista De Tecnologia) Na linguagem C#, para inserir um elemento no final de um ArrayList, deve ser utilizado o método:
a) Add.

b) AddToEnd.

c) Append.

d) Insert.

e) Put.

10. (VUNESP - 2013 - IMESC - Analista De Tecnologia) Analise o seguinte trecho de código em linguagem C#:
int x = 10;
int y = 20;

x. += x. == 20 ? x / y : y / x;
y -= y == 10 ? y / x : x / y;

Após a execução desse trecho de código, o valor das variáveis "x" e "y" serão, respectivamente,

a) 2 e 0.

b) 10 e 18.

c) 10 e 20.

d) 12 e 19.

e) 12e20.

11. (VUNESP - 2013 - MPE/ES - Agente Técnico - Desenvolvedor) Na linguagem C#, é possível dividir a definição de uma classe em diversos arquivos. Para tanto, é necessário que a declaração da classe contenha a palavra chave:
a) split b) partial c) extern d) continue e) abstract
12. (VUNESP - 2013 - MPE/ES - Agente Técnico - Desenvolvedor) Na linguagem C#, a forma correta de declarar a classe B, derivada da classe A, é:
a) public class B inherits A {}

b) public class B => A {}

c) public class A extends B {}

d) public class B : A {}

e) public class B implements A {}

13. (VUNESP - 2013 - MPE/ES - Agente Técnico - Desenvolvedor) Na linguagem C#f a palavra reservada "sealed" pode ser utilizada na declaração de classes. Ela tem a função de a) indicar que a classe possui métodos que precisam ser sobrescritos.
b) impedir que a classe seja instanciada mais de uma vez.

c) impedir que a classe seja derivada por outras classes.

d) garantir que a classe não seja instanciada por classes que não estejam no mesmo namespace.

e) indicar que o conteúdo da classe é imutável, isto é, uma vez instanciada, seu conteúdo não é mais alterado.
14.(AOCP - 2012-TCE/PA-Assessor Técnico - Analista De Sistemas) Em C#, os métodos chamados pelo mecanismo de execução do programa quando o objeto está prestes a ser removido da memória são denominados de:
a) Garbage Collection.

X 57

/

b) Destruidores.

c) Propriedades.

d) Indexadores.

e) Eventos.

15. (AOCP - 2012 - TCE/PA - Assessor Técnico - Analista De Sistemas) Analise o seguinte trecho do código C#:
(. . .)

01 double x = 1432.7;

02 int y;

03 y = (int)x;
(-)

Sobre a linha 03 do código apresentado, é correto afirmar que:

a) a variável y recebe o valor de x se esta última (x) for do tipo int.

b) atribui à variável y o valor da variável x convertido para o tipo int.

c) passa como parâmetro o valor da variável x para y, do tipo double.

d) a variável y recebe por referência o valor da variável x do tipo double.

e) multiplica o valor da variável int por x e atribui o valor calculado para a variável y.

16. (AOCP - 2012 - TCE/PA - Assessor Técnico - Analista De Sistemas) Segundo a
Microsoft, um conjunto de recursos introduzidos no Visual Studio 2010 que estende as capacidades de consultas à sintaxe da linguagem de C# e Visual Basic é conhecido como:
a) LINQ.

b) T-SQL.

c) OQL.

d) ADO.

e) ASP.

17. (AOCP - 2012 - TCE/PA - Assessor Técnico - Administrador De Banco
De Dados) Sobre a linguagem C# assinale a alternativa correta.
a) É uma linguagem de programação orientada a objetos, desenvolvida pela Microsoft como parte da plataforma .NET caracterizada por ser fracamente tipada.
, <

b) É a única linguagem de programação que suporta herança múltipla pura, ou seja, cada classe pode herdar características de uma ou mais classes.
c) A linguagem não suporta ponteiros porque os blocos de códigos requisitariam permissões mais altas de segurança para serem executados.
d) O garbage collection é um processo usado para a manutenção do processador evitando erros comuns que podem levar ao encerramento do programa.
e) Há três tipos de passagem de parâmetros, por valor, por referência e por saída.

18.(FCC - 2014-TRF3-Analista Judiciário - Informática)

x'

/ 57

/

Utilize o programa C# abaixo para responder as questões de números 43 e 44.

Os números à esquerda não fazem parte do programa, apenas indicam os números das linhas.

[1] using

[2] using

[3] using

[4] using

System;
System.Collections.Generic;
System.Linq;

System.Text;

[5] namespace ConsoleApplicationl

[6] {

[7] public static class ConverteTemp

[8] {

[9] public static double CelsiusToFahrenheit(string tempCelsius)

[10] {

[11] double celsius = Double.Parse(tempCelsius);

[12] double fahrenheit = (celsius *9/5) +32;

[13] return fahrenheit;

[14] }

[15] public static double FahrenheitToCelsius(string tempFahrenheit)

[16] {

[17] double fahrenheit = Double.Parse(tempFahrenheit);

[18] double celsius = (fahrenheit - 32) *5/9;

[19] return celsius;

[20] }

[21]

[22] }

[23] class TestaConverteTemp

[24] {

[25] static void MainO

[26] {

[27] Console.WriteLine("Selecione a conversão desejada");

[28] Console.WriteLine("1. De Celsius para Fahrenheit.");

[29] Console.WriteLine("2. De Fahrenheit para Celsius.");

[30] Console.Write(":");

[31] string opcao = Console.ReadLine();

[32] double F, C = 0;

[33] switch (opcao)

[34] { case "1": Console.Write("Digite a temperatura em Celsius: ");

[35] F = ConverteTemp.CelsiusToFahrenheit(Console.ReadLine());

[36] Console.WriteLine("Temperatura em Fahrenheit: {0:F2}"> F)

[37] break;

[38] case "2": Console.Write("Digite a temperatura em Fahrenheit: ");

[39] C = ConverteTemp.FahrenheitToCelsius(Console.ReadLine());

[40] Console.WriteLine("Temperatura em Celsius: {0:F2}", C);

[41] break;

[42] default: Console.WriteLine("Opcao invalida.");

[43] break;

[44] }

[45] Console.WriteLine("Pressione uma tecla para finalizar.");

[46] Console.ReadKey();

[47] )

[48] }

[49] }

O programa C# apresentado é executado apenas uma vez e finaliza. Para que o programa possa ser executado diversas vezes, até que o usuário digite 0 para finalizá-lo é necessário inserirConsole.Writel_ine("0. Finaliza."); como mais uma opção do menu e inserir a seguinte instrução de repetição:
a) while (opcao != 0) antes do switch, que está na linha 33, com os delimitadores de início e fim {} desta instrução envolvendo as linhas 33 a 44.
b) while (opcao != "0") antes do switch, que está na linha 33, com os delimitadores de início e fim {} da instrução envolvendo as linhas 33 a 44.
c) for (; ;) { após o delimitador de início de bloco { na linha 26
e uma chave } para fechar o bloco logo após a linha 44. Antes do switch, que está na linha 33,inserir o comando if (opcao

== "0") break;

d) do antes do switch, que está na linha 33, com o delimitador de início { da instrução envolvendo as linhas 33 a 44, e finalizando com o delimitador de fim } while (opcao != "0");
e) for (opcao=0;opcao<3;opcao++) após o delimitador de início de bloco { na linha 26 com os delimitadores de início e fim {} da instrução envolvendo as linhas 27 a 44.
19.(FCC - 2014 - TRF3 - Analista de Sistemas) Considerando o programa e a linguagem C#, é correto afirmar:
. a) Console é uma classe. As classes Object e System herdam desta classe.

b) Na linha [25]: Quando o aplicativo é iniciado, o método Main é o primeiro método invocado.Em C#, bibliotecas e serviços não requerem um método Main como um ponto de entrada.

c) WriteLine é um método da classe Console. Como a classe System herda da classe Console,então WriteLine também é um método da classe System.

d) Na linha [11 ]: double celsius = Double.Parse(tempCelsius); significa que double é uma classe e Parse é um método desta classe.
e) Na linha [42]: default é um atributo exclusivo do comando switch e é usado apenas quando um valor numérico que não conste dos cases é fornecido pelo usuário.
20. (CESPE - 2013 - BACEN - Analista De Sistemas)
class Teste

{

static void Main()

{

X 57

/

int num = 1;

while (num++ < 6)

{

Console.WriteLine ("num é = {0}", num);

}

}

}

Nessa situação, essa classe produz o seguinte resultado:

a) num é = 1

b) num é = 2

c) num é = 3

d) num é = 4

e) num é = 5

21.(CESPE - 2013 - BACEN - Analista De Sistemas) Em C#, o operador ?? é denominado operador de concentração de nulo e é usado para definir um valor padrão para tipos de valor anulável ou tipos de referência. No exemplo abaixo, caso a variável num seja nula, o valor de x será igual a
1. int x = num ?? 1;

22. (CESGRANRIO - 2013 - IBGE - Analista De Sistemas) O que ocorre com o programa C#,apresentado abaixo, quando é compilado e posteriormente executado?

using System;
publlc cla.33 Prova

{

public static void Main()

{

int[] a=new int[10];
int 1=0;

while {

a[i] = 1 + (i>0 ? a[i-l] : 0) ;
1++ r

Console.WrlreLine(a[9]);

a) Compila corretamente, executa e imprime o número 45.

b) Compila corretamente, executa e imprime o número 9.

c) Compila corretamente e executa, mas nunca termina.

d) Compila corretamente, mas apresenta erro de execução.

e) Apresenta erro na compilação.

23.(CESGRANRIO - 2012 - EPE - Analista De Gestão Corporativa - Tecnologia
Da Informação) Na programação orientada a objeto, na linguagem C# em particular, a capacidade de construir vários métodos com um mesmo nome, porém com parâmetros diferentes na mesma classe, é chamada de a) Polimorfismo universal b) Polimorfismo paramétrico c) Polimorfismo de subtipo d) Sobrecarga de operadores e) Sobrecarga de métodos
24. (CESGRANRIO - 2010 - ELETROBRAS - Analista De Sistemas - Engenharia
De Software) O
programador de um sistema Web deseja imprimir, em determinada tela, a hora atual. Que fragmento de código C# atinge esse objetivo?
a) Now.ToStringO;

b) DateTime.Now.ToString( HH:mm );

c) DateTime.Actual.ToString( HH:mm );

d) Time.Now.ToString( HH:mm );

e) Now.ToString( HH:mm );

25. (CESGRANRIO - 2010 - EPE - Analista De Gestão Corporativa - Tecnologia
Da Informação)
Determinado órgão público federal deseja implantar um sistema de consulta na
Internet. A
plataforma utilizada será ASP.NET e a linguagem de programação, C#. Na modelagem orientada a objetos desse sistema, é importante considerar que a linguagem adotada:
a) impede, no contexto de instanciação de objetos, o uso de classes abstratas.

b) impede somente o uso de polimorfismo a fim de assegurar a legibilidade do código.

c) apresenta o conceito de namespaces para implementar associações entre classes.

d) proíbe o uso de interfaces para garantir a coesão e a modularidade do código.

e) implementa, no âmbito da generalização, somente herança simples.

26. (FGV - 2016 - IBGE- Análise De Sistemas - Desenvolvimento De Sistemas) Analise o código C#exibido a seguir:

using System;
namespace ENIGMA

{

class Program {

static void Main(string[] args) {
P d = new P();

d.PPO;

E s = new E();
s.A();

s.PP();

Console.ReadKeyO;

}

class P {

public void PPO

{

Console.WriteLine("PP");

}

}

class E : P {
public void A()

{

Console.Writel_ine("A");

}

O resultado produzido no console é:

a) PP
A
PP

b) PP
PP

c) A
PP
A

d) AA

P
AA

e) A
A
A

27.(FGV - 2016 - IBGE - Análise De Sistemas - Desenvolvimento De Sistemas)
using System;

namespace TESTE

/ 57

/

{

class Program

{

delegate int del(int i);

static void Main(string[] args)

{

dei myF = x => x * x;
int j = myF(5); //j = 25

Console.WriteLine(j.ToStringO);

}

}

}

O resultado produzido no console é:

a) 5

b) 25

c) False d) True e) x * x
GABARITo

GABARITO

1. E 6. A
11. B

2. B 7. A
12. D

3. B 8. E
13. C

4. B 9. A
14. B

5. A 10. E
15. B

16. A

17. E

18. C

19. B

20. Errado

21. Certo

22. A

23. E

24. B

25. E

26. A

27. B

SERPRO (Analista - Especialização: Tecnologia) Desenvolvimento de software - 2023 (Pós-I

