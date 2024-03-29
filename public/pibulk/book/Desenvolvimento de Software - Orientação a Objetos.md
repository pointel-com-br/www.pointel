# Desenvolvimento de Software - Orientação a Objetos

Índice

1) Programação Orientada a Objetos - Conceitos Básicos

2) Questões Comentadas - Programação Orientada a Objetos - Conceitos Básicos - Multibancas

3) Questões Comentadas - Programação Orientada a Objetos - Conceitos Básicos - FCC

4) Questões Comentadas - Programação Orientada a Objetos - Conceitos Básicos - Cebraspe ...

5) Lista de Questões - Programação Orientada a Objetos - Conceitos Básicos - Multibancas

6) Lista de Questões - Programação Orientada a Objetos - Conceitos Básicos - FCC

7) Lista de Questões - Programação Orientada a Objetos - Conceitos Básicos - Cebraspe

PRoGRAMAçÃo ORIENTADA A OBJEToS

What OOP users claim

Brincadeirinha, hein, galera, Programação Orientada a Objetos (POO) é muito importante!! :DGalera, vamos ver nessa aula toda a aplicação dos conceitos do paradigma de orientação a objetos, ou seja, como isso funciona na prática! Como é impossível mostrarmos como programar orientado a objetos em todas as linguagens, vamos apresentar todas as implementações usando a linguagem Java!
Professor, mas C++, Python, PHP não são linguagens orientadas a objetos também?
São sim,
padawan (PHP também suporta, lembremos!) mas a mais cobrada, DISPARADO, é Java: motivo suficiente para fecharmos com ela. Essa matéria é bem "bola dividida", pois os conceitos de OOsão considerados engenharia de software. Desse modo, nesse curso vamos focalizar mesmo na implementação! Vamos nessa?
A Orientação a Objetos tem alguns pilares que devem ser implementados em qualquer linguagem de programação. Muitas linguagens procedurais possuem caraterísticas semelhantes à orientação a objetos, como a similaridade dos registros em C com classes, mas isso não basta que algumas dessas características estejam presentes para ser considerada uma linguagem orientada a objetos!Professor, e quais são esses pilares?? Padawan, nunca se esqueça, uma linguagem de programação só pode ser chamada de OO se tiver suporte nativo a: Encapsulamento,Herança,
Composição e Polimorfismo. Alguns autores afirmar que as quatro caraterística na verdade são somente uma: o princípio da abstração.
Mas vamos começar pela pedra fundamental, classes e objetos.

/ 44

/

Classes

A classe é a planta ou esquema que indica como os objetos são criados,
quais os seus comportamentos e variáveis de estado. Para declarar uma classe, é necessário utilizar a sintaxe a seguir:
[palavra-chave] class NomeDaClasse {

//Atributos e Métodos

}

Portanto para declarar uma classe, deve-se colocar a palavra class seguida de um identificador que irá servir de nome para a classe. O identificador pode ser qualquer palavra, exceto palavras reservadas. Por exemplo: class Conta introduz a declaração de uma nova classe chamadaConta.
Note que, por convenção, o nome de uma classe inicia sempre com uma letra maiúscula.
A Palavra-
Chave é opcional, podendo ser:

//Essa classe pode ser acessada por todos public class Carro {...}
//Essa classe não pode gerar instâncias abstract class Carro {...}
//Essa classe não pode ser estendida final class Carro {...}
Objetos

Um objeto é uma instância de uma classe. Para criar um objeto, devemos utilizar a seguinte sintaxe:
new construtorQ;

O comando new, também conhecido como operador de criação, cria um novo objeto, alocando memória para o objeto e inicializando essa memória para valores default. Ele necessita de um operando: o construtor, que é o nome de um método especial que constrói o objeto.Uma vez x' 4
/ 44

/

construído, o objeto deve ser atribuído a uma variável, para que possa ser utilizado e referenciado no futuro.
/* 1) Operador NEW é responsável por criar um objeto;

* 2) NomeClasseO é o construtor da Classe NomeClasse;

* 3) NomeObjeto é uma variável do Tipo NomeClasse; */

NomeClasse NomeObjeto = new NomeClasseO;

/* Observem que é possível atribuir o objeto de uma

* classe para uma variável de outra classe */

A linguagem Java assume a responsabilidade de destruir qualquer objeto criado que não esteja sendo usando. Para tal, utiliza um Coletor de Lixo (Garbage Collector), que é executado em intervalos regulares, examinando cada objeto para ver se ele ainda é referenciado por alguma variável. Caso o objeto não seja utilizado ao menos por uma variável, ele é destruído e sua memória é liberada.
Atributos

Um atributo ou campo é uma variável declarada no corpo de uma classe. Ele serve para armazenar o estado de um objeto (atributo de instância) ou o estado de uma classe (atributo de classe). Asintaxe de declaração de um atributo é a seguinte:

[palavra-chave] tipoAtributo NomeAtributo [=expressão];
A Palavra-Chave é opcional, podendo ser:

Final, Volatile, Static ou Transient class Empregado {
final String Nome; //Indica que Nome é um atributo constante;

volatile Salario; //Indica que Salário é modificável por threads distintas;
static Idade; //Indica que Idade é compartilhada por todos objetos;

/ 44

/

transient Sexo; //Indica que Sexo não pode ser serializável;

}

Modificadores de Acesso:

class Empregado {

public String nome; //Nome: público private int Salario; //Salário: privado protected short Idade; //Idade: protegido char Sexo; //Sexo: default
}

Métodos

Java utiliza métodos para se referir a trechos de código que são associados a classes. Se os atributos servem para manter ou armazenar o estado ou o valor de um objeto, os métodos servem para descrever os comportamentos de um objeto ou classe. Um método é muito similar a uma função em C. A maior diferença é que os métodos da linguagem Java são declarados completamente dentro de uma classe.
[Palavras-Chave] TipoRetorno NomeMetodo ([Lista de Parâmetros])

{

//Corpo do Método

}

A sintaxe de declaração de um método é apresentada acima. A Palavra-Chave é opcional,podendo ser:

Abstract, Final, Static, Native e Synchronized

//Indica que esse método não possui corpo abstract int soma (int a, int b) {//...//}
/ 44

/

//Indica que esse método não pode ser sobrescrito final int soma (int a, int b) {//...//}
//Indica que esse método só pode acessar atributos de classe e não pode ser sobrescrito static int soma (int a, int b) {//...//}
//Indica que esse método foi escrito outra linguagem native int soma (int a, int b) {//...//}
//Indica que esse método só é executável por uma thread por vez synchronized soma (int a, int b) {//...//}
Modificadores de Acesso:

public int soma (int a, int b) {//...//}
private int soma (int a, int b) {//...//}
protected int soma (int a, int b) {//...//}
int soma (int a, int b) {//...//}

Vamos falar agora sobre um método importante: Construtor! Ele é um método especial,
chamado pelo operador new quando um novo objeto necessita ser criado. Dentro do construtor, pode-se colocar código customizado de inicialização do objeto. Em geral, ele deve ter o mesmo nome da classe em que for declarado. Além disso, um construtor não deve ter um tipo de retorno em sua declaração.
Professor, não entendo uma coisa! Em geral, no código da classe não há nenhum método com o nome do método construtor. Ora, não há declaração de método algum! Como é isso? Éverdade!
Basicamente, quando você não declara um construtor para uma classe, o compilador cria um construtor padrão com uma lista vazia de parâmetros. Pode-se criar diversos construtores para uma mesma classe.
/ 44

/

Outro método muito importante é o Método Main! Pois é, ele é sempre definido como um método de classe, i.e., possui um modificador static:
public static void main (String[] args) throws java.lang.Exception

Interface

Galera, o que é uma Interface? É simplesmente um contrato! Quando vocês assinam o contrato do seguro de um carro, vocês estão se comprometendo a atender aquilo que lá está escrito.Analogamente, a interface é um contrato que obriga aqueles que a assinam a implementar os métodos lá presentes. Elas ajudam a padronizar implementações - entradas e saídas.
Em outras palavras, é um recurso utilizado em Java para obrigar a um determinado grupo de classes a ter métodos ou propriedades em comum para existir em um determinado contexto,contudo os métodos podem ser implementados em cada classe de uma maneira diferente. Em geral, as interfaces são compostas basicamente de um conjunto de assinaturas de métodos públicos e abstratos.
public interface FiguraGeometrica {
public String getNomeFigura();
public int getArea(int vertice);
public int getPerimetroO;

}

A sintaxe para implementar uma Interface utiliza a palavra reservada implements:
public class ClasselmplementadoraDelnterfaces implements FiguraGeometrica

Professor, qual a diferença entre uma Interface e uma Classe Abstrata? Bem, Interfaces não são classes; são, na verdade, entidades que não possuem qualquer implementação, apenas assinatura,sendo que todos os seus métodos são públicos e abstratos. Já as Classes
Abstratas também contêm, em geral, métodos abstratos (sem corpo), mas podem ter vários métodos concretos.
Uma Classe Abstrata pode, inclusive, não conter nenhum método abstrato, i.e.,
todos os seus métodos são concretos. No entanto, se uma classe tiver um único método abstrato que seja, ela será considerada uma Classe Abstrata. Aliás, uma Interface é também chamada de classe abstrata pura por conta disso, ou seja, não há impurezas (isto é, métodos concretos).
/ 44

/

Encapsulamento

Pessoal, nós já sabemos que para se descobrir o que um objeto pode fazer, basta olhar para as assinaturas de seus métodos públicos definidos na classe desse objeto - que formam uma interface de uso. A assinatura de um método é composta pelo seu nome e seus parâmetros. Por outro lado,para descobrir como um objeto realiza suas operações, deve-se observar o corpo de cada um dos métodos da classe.
Os corpos dos métodos constituem a implementação das operações dos objetos. Professor,
por que nós encapsulamentos classes, atributos e métodos? Cara, por duas razões:desenvolvimento e manutenibilidade. O encapsulamento ajuda a aumentar a divisão de responsabilidades (ou coesão) e, dessa forma, fica mais fácil e rápido desenvolver sistemas em módulos.
Da mesma forma, ele ajuda a manutenção, visto que para torna-se mais difícil fazer
"besteiras" no código e atrapalhar manutenções futuras. Trazendo isso para a vida real, lidamos com encapsulamento o tempo inteiro. Você sabe como usar um controle remoto, mas você não sabe como ele funciona internamente. Encapsula-se seu funcionamento interno e disponibiliza-se apenas sua interface ao usuário.
Chegamos ao conceito de Modificadores de Acesso! Eles são utilizados para modificar o modo como classes, métodos e variáveis são acessadas. Existem três modificadores de acesso e um quarto nível (acesso default/friendly), quando não se usa nenhum dos modificadores citados. Toda classe, método e variáveis de instância declaradas possuem um controle de acesso.
Pessoal, esses Modificadores de Acesso determinam quão acessíveis são esses elementos.
Vamos vê-los agora em mais detalhes:
<public>: essa instrução indica que a classe, método ou atributo assim declaradas podem ser acessadas em qualquer lugar e a qualquer momento da execução do programa -é o modificador menos restritivo.
<private>: essa instrução indica que métodos ou atributos (classes, não)
assim declaradas podem ser acessadas apenas dentro da classe que os criou. Subclasses herdam-nos, mas não os acessam - é o modificador mais restritivo1.
<protected>: essa instrução indica que métodos ou atributos (classes, não) assim declaradas somente podem ser acessadas dentro do pacote em que está contida ou por subclasses no mesmo pacote.
1 Em tese, no Mundo Java, classes não herdam nem acessam membros privados - objetos herdam membros privados, mas não o acessam. A documentação oficial afirma da seguinte forma: 11 Members of a dass that are dedared private are not inherited by subdasses o f that dass".
/

<default>: também chamado friendly, não há palavra para esse modificador porque ele é, na verdade, a ausência de um modificador. Indica-se que a classe, método ou atributo podem ser acessadas por classes do mesmo pacote.
Especificador Própria Classe Subclasse Pacote Global
Privado (-) Sim Não Não
Não

<Vazio> (~) Sim Não* Sim
Não
Protegido (#) Sim Sim Sim
Não
Público (+) Sim Sim Sim
Sim

OBSERVAÇÃO

É importante ressaltar que, em caso de não haver modificador, a subclasse pode ou não acessar os métodos e atributos da sua superclasse, e isso depende da localização da subclasse.Se ela estiver em um pacote diferente do pacote da superclasse, não poderá acessar.
Se estiver em um mesmo pacote da superclasse, poderá acessar. Logo, para diferenciar o ModificadorPacote do Modificador Protegido, deve-se saber primeiramente se é desejável que a subclasse possa ter acesso a atributos e métodos da classe.
Pensem comigo! Acessar ou editar propriedades de objetos, manipulando-as diretamente, pode ser muito perigoso e gerar muitos problemas. Por conta disso, é mais seguro, para a integridade dos objetos e, consequentemente, para a integridade da aplicação, que esse acesso ou edição sejam realizados através de métodos desse objeto.
Utilizando métodos, podemos controlar como consultas e modificações são realizadas,controlando-as. Para tal, podemos utilizar Métodos Getters e Setters - para recuperar dados e inserir dados, respectivamente. Para o primeiro, utiliza-se o Método Get; para o segundo, utiliza-se o Método Set. Em geral, costuma-se declarar atributos como privados, e métodos e classes como públicos.
class Classel {

//Atributo privado private String Algo;
/ 44

/

//Método público para recuperar dados public String getAlgo() {
return this.Algo;

}

//Método público para modificar/inserir dados public void setAlgo(String Algo) {
this.Algo = Algo;

}

}

Polimorfismo

A palavra Polimorfismo vem do grego: muitas formas. Trata-se da capacidade de um objeto poder se comportar de diversas formas dependendo da mensagem recebida. Observem que isso não quer dizer que o objeto fica transformando seu tipo a todo momento. Na verdade, um objeto nasce com um tipo e morre com esse mesmo tipo. O que muda, então? É a forma como nós nos referimos a esse objeto!
Existem dois tipos de polimorfismo:

Polimorfismo Estático: ocorre quando uma classe possui métodos com mesmo nome,entretanto assinaturas diferentes, i.e., métodos de uma mesma classe se sobrecarregando.Pode ser chamada também de Sobrecarga ou Overloading. Ocorre em Tempo de Compilação e alguns não o consideram um tipo de polimorfismo, porque a assinatura é diferente.
Polimorfismo Dinâmico: ocorre quando uma classe possui um método com mesmo nome e mesma assinatura que um método de sua superclasse, i.e., o método da classe-filha sobrescreve o método da classe-pai. Pode ser chamada também de Sobrescrita,Overriding,
Redefinição ou Sobreposição. Ocorre em Tempo de Execução e é um corolário do conceito de herança.
Professor, o que você quer dizer com mesma assinatura e assinatura diferente?
É a mesma quantidade, tipo e ordem dos parâmetros. Em outras palavras:
/ 44

/

//Assinatura Igual: quantidade, tipo e ordem public String EntendendoAssinatura(int A, char B);public String EntendendoAssinatura(int C, char D);

//Assinatura Diferente: quantidade diferente public String EntendendoAssinatura(long A, long B, long C);public String EntendendoAssinatura(long A, long B);

//Assinatura Diferente: tipo diferente public String EntendendoAssinatura(long A, long B);public String EntendendoAssinatura(char A, long B);

//Assinatura Diferente: ordem diferente public String EntendendoAssinatura(int A, char B);public String EntendendoAssinatura(char B, int A);

Agora vamos ver um exemplo de Polimorfismo Dinâmico. Eu pensei comigo mesmo: O que seria uma característica comum de praticamente todos os animais? Emitir sons! Observem que eu criei uma classe abstrata que possui um único método - também abstrato que não retorna valor algum e não recebe nenhum argumento. Vejam a classe abaixo:
abstract class Animal {
abstract void som();

}

Dito isso, vou criar dois animais do meu gosto pessoal: um gato e um cachorro! Bem,
o gato é um animal! Que relacionamento é esse "é um"? Herança! Portanto as classes gato e cachorro serão classes filhas da superclasse Animal. Observem abaixo que ambas implementam o método
, 44

abstract void som( ), porém cada uma a sua maneira, visto que gatos e cachorros emitem sons diferentes!
class Gato extends Animal {
void som() {

System.out.println("MIAU!");

class Cachorro extends Animal {
void som() {

System.out.println("AUAU!");

Pois bem! Vamos ver agora o Polimorfismo Dinâmico em ação. Criaremos um objeto do tipo Gato e atribuiremos a um objeto do tipo Animal. Professor, você pode fazer isso? Sim,porque Gato é filho de Animal - é similar a um casting implícito! Em seguida chamaremos o método som(). Por fim, faremos o mesmo procedimento com o objeto do tipo Cachorro.
public static void main(String[] args) {
Animal animal = new Gato();
animal.som(); //Emite o som MIAU!
Animal animal = new CachorroO;
animal.som(); //Emite o som AUAU!

}

Olha que bacana: existem dois métodos com exatamente o mesmo nome e mesma assinatura!
Como o compilador saberá qual deve ser chamado? Ele não saberá - tem que ser em tempo de execução. No primeiro momento, ele apresentará "MIAU!", porque animal é nesse instante um
/ 44

/

gato. Depois fazemos outra atribuição e ele apresentará "AUAU", porque animal naquele instante é um cachorro.
O Polimorfismo Estático é bem mais simples! Imaginem que eu deseje fazer dois cálculos matemáticos. Primeiro somar três números e depois somar apenas dois números. Eu posso ter dois métodos com mesmo nome, mas assinaturas diferentes. Dessa forma, se eu passar três valores, ele saberá que é um método; e se eu passar dois valores, ele saberá que é outro método.Simples, não?

class Calculo {

void soma(int a,int b){
System.out.println(a+b);

}

void soma(int a,int b,int c){
System.out.println(a+b+c);

}

public static void main(String args[]) {
Calculo x = new CalculoO;

x.soma(10,10,10); //Mesmo nome, mas assinatura diferente (3 valores)

x.soma(20,20); //Mesmo nome, mas assinatura diferente (2 valores)

}

}

Java: Herança

Herança é a habilidade de se derivar alguma coisa específica a partir de algo mais genérico. Nós encontramos essa habilidade ou capacidade diversas vezes em nosso cotidiano. Por exemplo: umPálio estacionado na garagem do seu vizinho é uma instância específica da categoria
Carro, mais genérica. Da mesma forma, uma Honda CG 125 é uma instância específica da categoria mais genérica Moto.
Se levarmos as categorias Carro e Moto para um outro nível mais elevado, as duas se relacionarão uma com a outra por serem instâncias específicas de uma categoria mais genérica ainda que elas:a categoria Veículo. Em outras palavras, carros e motos são veículos. A
imagem abaixo esquematiza as relações entre Pálio, Carro, Honda CG 125, Moto e Veículo.
4-IONP^ CGj

Esse exemplo ilustrou a Herança Simples! Neste caso, uma entidade herda estados e comportamentos (atributos e métodos) de uma e somente uma categoria. O Pálio, por exemplo,herda da categoria Carro (e somente dela, diretamente). Em contraste, a Herança
Múltipla permite

/

que uma entidade herde diretamente comportamentos e estados de duas ou mais categorias ao mesmo tempo.
Imagine um Empregado chamado José de uma empresa qualquer. Para ser mais específico,
pense em José como sendo tanto Gerente quanto Contador simultaneamente dessa empresa.Ele herdaria as capacidades de um Gerente e de um Contador, concordam? Portanto,em uma hierarquia de entidades, João herdaria de duas classes diferentes diretamente, como apresenta a imagem abaixo:
JOIAO

A sintaxe da herança sugere que você pode estender uma e somente uma classe. O Java não suporta Herança Múltipla, porque - segundo projetistas da linguagem -esse tipo de implementação poderia gerar confusão. Imagine, por exemplo, duas classes-base declarando um atributo que possua o mesmo nome, mas com tipos diferentes. Qual dos dois a classe-filha deveria herdar?
A mesma situação poderia acontecer com um método! Se dois métodos possuíssem o mesmo nome, mas diferentes listas de parâmetros ou tipos de retorno, qual deles a subclasse deveria herdar? Vocês percebem como isso poderia causar inconsistências de projeto? Para prevenir tais problemas, a linguagem Java rejeita a implementação de herança múltipla.
Novas classes derivam capacidades (expressas como atributos e métodos) de classes já existentes.Isso faz com que o tempo de desenvolvimento de uma aplicação seja bem menor, pois classes já existentes e comprovadamente funcionais (livres de erros e já testadas) são reaproveitadas (ou reutilizadas). A sintaxe que expressa o conceito de extensão de classes é a seguinte:
class NomeClasseFilha extends NomeClassePai {

//Atributos e Métodos

}

Essa sintaxe pode ser lida da seguinte forma: NomeClasseFilha estende
NomeClassePai. Em outras palavras, NomeClasseFilha herda (ou deriva) capacidades (expressas através de atributos e métodos) de NomeClassePai. A NomeClasseFilha é conhecida como subclasse, classe derivada ou classe-filha e NomeClassePai é conhecida como superclasse, classe-base ou classe-pai.
A palavra-chave extends faz com que uma subclasse herde (receba) todos os atributos e métodos declarados na classe-pai (desde que ela não seja final), incluindo todas as classes-pai da classe-pai.A classe-filha pode acessar todos os atributos e métodos não-privados. Ela herda, mas não acessa(ao menos diretamente) métodos e atributos privados.

Todo objeto criado a partir de uma subclasse é também um objeto do tipo da sua superclasse (Ex:um objeto do tipo Carro também é um objeto do tipo Veículo). Essa afirmação implica o fato de que você pode atribuir um objeto de uma subclasse para uma referência criada ou declarada para um objeto de sua superclasse. Como assim, professor? Vejamos!
//Objeto do tipo Carro é um objeto do tipo Veículo
Veiculo v = new CarroQ;

A linha de código acima cria um objeto do tipo Carro e atribui sua referência à variável v. Note que essa variável v é uma variável que armazena referências para objetos do tipoVeículo. Esse tipo de atribuição é perfeitamente possível, já que um Carro é uma subclasse deVeículo. Através da variável v, é possível chamar os métodos que pertencem ao tipo Veículo.
Portanto, pode-se utilizar esse artifício de nomeação para transformar uma classe-filha em qualquer uma de suas classes-pai. Professor, é possível fazer o inverso?Pode-se atribuir uma classe-pai a uma classe-filha? Não, isso só pode ser feito por meio de um type cast.Assim, uma variável pode assumir momentaneamente outro tipo para que o programador possa utilizá-la.
Legal, galera! Vamos ver agora como são cobradas as questões de programação OO em Java!

/ 44

/

QUESTõES CoMENTADAS - PRoGRAMAçÃo ORIENTADA A

OBJEToS - MULTIBANCAS

1. (FUNCAB - 2010 - PRODAM-AM - Analista de TI - Desenvolvimento de Sistemas) Seja a seguinte classe Java:
<mod> public class Xpto

{

J

Qual das alternativas a seguir contém um modificador que ao ser usado na declaração acima em substituição ao termo <mod> impedirá que a classe Xpto seja estendida?
a) static b) const c) abstract d) final e) virtual
Comentários:

//Essa classe não pode ser estendida final class Carro {...}
Conforme vimos em aula, trata-se do Final. Gabarito: D

2. (CESGRANRIO - 2012 - Petrobrás - Técnico de Exploração de Petróleo
Júnior -
Informática) Ao escrever o código da Classe PortaDeCofre em Java para que ela atenda a interface Porta, como um programador deve começar a declaração da classe?
a) public class Porta:PortaDeCofre {

b) public class PortaDeCofre :: Porta {

c) public class PortaDeCofre inherits Porta {

d) public class PortaDeCofre extends Porta {

e) public class PortaDeCofre implements Porta {

Comentários:

A sintaxe para implementar uma Interface utiliza a palavra reservada implements:
public class Teste implements FiguraGeometrica

Conforme vimos em aula, utilizamos a palavra-reservada implements. Gabarito: E

/ 44

/

3. (ESAF - 2008 - CGU - Tecnologia da Informação) Com relação a essa característica, é correto afirmar que:
a) métodos declarados como public em uma superclasse, quando herdados,
precisam ser protected em todas as subclasses dessa classe.
b) métodos declarados como protected em uma superclasse, quando herdados, precisam ser protected ou public nas subclasses dessa classe.
c) o nível de acesso protected é mais restritivo do que o nível de acesso default.

d) métodos declarados como public só podem ser acessados a partir dos métodos da própria classe ou de classes derivadas.
e) métodos declarados como default só podem ser acessados a partir dos métodos da própria classe.
Comentários:

(a) Não, essa afirmação não faz qualquer sentido; (b) Sim, as subclasses nunca podem ser mais restritivas que as superclasses; (c) Não, default é mais restritivo; (d) Não, eles podem ser acessados por quaisquer métodos de quaisquer classes ou pacotes; (e) Não, eles podem ser acessados pela própria classe, pelas subclasses e pelas classes do mesmo pacote. Gabarito: B
4. (FGV - 2015 - PGE/RO - Analista de Sistemas) Na linguagem de programação Java,
para indicar que uma classe A é derivada de B, utiliza-se, na declaração de A, o modificador:
a) imports;

b) extends;

c) inherits;

d) subclass;

e) superclass.

Comentários:

A palavra-chave extends faz com que uma subclasse herde (receba) todos os atributos e métodos declarados na classe-pai (desde que ela não seja final), incluindo todas as classes-pai da classe-pai.A classe-filha pode acessar todos os atributos e métodos não-privados. Ela herda, mas não acessa(ao menos diretamente) métodos e atributos privados.

Conforme vimos em aula, trata-se do extends. Gabarito: B

5. (FGV- 2014 -TJ/GO- Analista de Sistemas) Se uma classe na linguagem Java é declarada com o modificador abstract, então essa classe:
a) não pode ser referenciada;

b) não pode ser estendida;

/ 44

/

c) não pode ser instanciada;

d) pode ser instanciada apenas uma vez;

e) não pode possuir métodos estáticos.

Comentários:

Aplicado a um método ou classe indica que a implementação completa deste método ou classe é efetuada posteriormente, por uma subclasse. Caso seja uma classe, significa que ela não pode ser instanciada.
Conforme vimos em aula, ela não pode ser instanciada. Gabarito: C

6. (FGV - 2014 - TJ/GO - Analista de Sistemas) Na linguagem de programação Java, uma classe declarada com o modificador final:
a) não pode ser instanciada;

b) não pode ser estendida;

c) pode ter o modificador abstract também presente na declaração;

d) não pode ter métodos estáticos;

e) não pode ter métodos de instância.

Comentários:

Portanto para declarar uma classe, deve-se colocar a palavra class seguida de um identificador que irá servir de nome para a classe. O identificador pode ser qualquer palavra,exceto palavras reservadas. Por exemplo: class Conta introduz a declaração de uma nova classe chamadaConta.
Note que, por convenção, o nome de uma classe inicia sempre com uma letra maiúscula. A Palavra-Chave é opcional, podendo ser:

//Essa classe pode ser acessada por todos public class Carro {...}
//Essa classe não pode gerar instâncias abstract class Carro {...}
//Essa classe não pode ser estendida

/ 44

/

final class Carro {...}

Conforme vimos em aula, ela não pode ser instanciada. Gabarito: B

7. (FGV - 2015 - TJ/BA - Analista de Sistemas) Em Java, os métodos declarados sem modificadores em uma interface são implicitamente:
a) públicos e estáticos;

b) públicos e abstratos;

c) privados e estáticos;

d) públicos e finais;

e) privados e abstratos.

Comentários:

Galera, se o método é declarado sem modificador dentro de uma interface,
então ele é implicitamente público e evidentemente abstrato. Gabarito: B
/ 44

/

QUESTõES CoMENTADAS - PRoGRAMAçÃo ORIENTADA A

OBJEToS - FCC

1. (FCC - 2009 - TJ-SE - Técnico Judiciário - Programação de Sistemas)
Um objeto é instanciado em Java por meio do operador:
a) instanceof.

b) extend.

c) new.

d) this.

e) type.

Comentários:

Testa se um objeto é uma instância de uma classe específica ou se é null.
Utilizado para aplicar o conceito de herança para uma classe, onde uma classe receberá os métodos e variáveis de instância da classe chamada de pai.
Utilizada para se criar novas instâncias de objetos.

Representa a instância que está atualmente sendo executada.

Conforme vimos em aula, trata-se da palavra-reservada new - lembrando que type não é um operador! Gabarito: C
2. (FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da
Informação)
Uma classe Java pode ser instanciada por um comando, cuja sintaxe é:

a) nome_Objeto nome_Classe = new nome_Objeto();

b) nome_Classe nome_Objeto = new nome_Classe();

c) nome_Classe nomejnstancia = new nome_Objeto();

, 44

d) nomejnstancia nome_Objeto = new nome_lnstancia();

e) nomejnstancia nome_Classe = new nomejnstancia();

Comentários:

/* 1) Operador NEW é responsável por criar um objeto;

* 2) NomeClasseO é o construtor da Classe NomeClasse;

* 3) NomeObjeto é uma variável do Tipo NomeClasse; */

NomeClasse NomeObjeto = new NomeClasseO;

/* Observem que é possível atribuir o objeto de uma

* classe para uma variável de outra classe */

Conforme vimos em aula, o operador new cria um novo objeto! Para tal, utiliza-se o construtor da classe que se deseja criar uma instância: Nome_Classe(). Por fim, ele atribui esse novo objeto a uma variável NomejDbjeto pertencente a classe Nome_Classe. Gabarito: B
3. (FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da
Informação) A
diretiva public é utilizada em Java para aplicar a encapsulação pública:

a) aos métodos e classes, apenas.

b) aos atributos, métodos e classes.

c) às classes, apenas.

d) aos atributos, apenas.

e) aos atributos e classes, apenas.

Comentários:

Pessoal, esses Modificadores de Acesso determinam quão acessíveis são esses elementos.
Vamos vê-los agora em mais detalhes:
<public>: essa instrução indica que a classe, método ou atributo assim declaradas podem ser acessadas em qualquer lugar e a qualquer momento da execução do programa - é o modificador menos restritivo.
Conforme vimos em aula, o public pode ser aplicado a atributos, métodos e classes. Gabarito: B

4. (FCC - 2008 - TCE-AL - Programador) Em Java, para alterar a visibilidade do elemento em que se aplica, entre outros, utiliza-se o modificador de acesso:
a) static.

b) abstract.

c) protected.

/ 44

/

d) volatile.

e) transient.

Comentários:

Pessoal, esses Modificadores de Acesso determinam quão acessíveis são esses elementos.
Vamos vê-los agora em mais detalhes:
<protected>: essa instrução indica que métodos ou atributos (classes, não)
assim declaradas somente podem ser acessadas dentro do pacote em que está contida ou por subclasses no mesmo pacote.
Apenas um desses é um Modificador de Acesso: protected. Gabarito: C

5. (FCC - 2005 - TRE-MG - Técnico Judiciário - Programação de Sistemas) Os métodos
Java que não retornam valores devem possuir no parâmetro tipo-de-retorno a palavra:
a) static.

b) public.

c) void.

d) main.

e) string args.

Comentários:

Conforme vimos em aula, trata-se da palavra-reservada void. Gabarito: C

6. (FCC - 2012 - MPE-AP - Analista Ministerial - Tecnologia da Informação) Analise o código das classes a seguir presentes em um mesmo pacote de um projeto Java:
public class NewClassA {

public double calcular(int x, int y) {
return x + y;

}

public double calcular(double x, double y) {

x'

/ 44

/

return x * y;

}

}

public class NewClassB extends NewClassA {

}

public class Start {

public static void main(String[] args) {

}

}

Com base nos códigos apresentados e nos conceitos da orientação a objetos é correto afirmar:
a) No método main da classe Start não é possível instanciar objetos das classes
NewClassA e
NewClassB, pois essas classes não contêm um construtor válido.

b) Se for digitada a instrução NewClassB c = new NewClassA(); no método main da classe Start será instanciado um objeto da NewClassA.
c) Se for digitada a instrução NewClassA b = new NewClassB(); no método main da classe Start ocorrerá um erro, pois não é possível criar um objeto da NewClassA por meio do construtor daNewClassB.

d) A existência de dois métodos de mesmo nome na NewClassA que recebem a mesma quantidade de parâmetros indica que está ocorrendo uma sobrescrita de métodos.
e) Por meio de um objeto da NewClassB será possível acessar os métodos presentes naNewClassA.

Comentários:

(a) Não, mesmo que não tenha um construtor explícito, o compilador cria um construtor padrão no momento da criação do objeto; (b) Não, não se pode atribuir uma instância de classe-pai a variável de uma classe-filha; (c) Não, não haveria erro! Pode-se atribuir uma instância de classe filha a variável de uma classe-pai; (d) Não, isso é sobrecarga; (e) Perfeito, ela herda tudo da classe-pai.Gabarito: E

7. (FCC - 2012 - TRE-CE - Técnico Judiciário - Programação de Sistemas) Com relação a herança na programação orientada a objetos com Java, é INCORRETO afirmar:
a) Uma subclasse herda os métodos da superclasse, entretanto, pode ter seus próprios métodos.
/ 44

/

b) Quando se instancia um objeto da subclasse, podem ser passados valores para os atributos da superclasse.
c) Um objeto da subclasse pode ser um objeto da superclasse.

d) Em uma superclasse, para acessar métodos da subclasse deve ser usada a instrução super.

e) Para definir que a subclasse herda as características da superclasse utiliza-se a instrução extends na declaração da subclasse.
Comentários:

(a) Perfeito, ela pode criar seus próprios métodos; (b) Perfeito, porque eles são herdados; (c)Perfeito, eles são herdados da superclasse; (d) Não, super é utilizado para acessar métodos da superclasse; (e) Perfeito, esse operador indica que a superclasse será estendida. Gabarito: D
8. (FCC - 2011 - TRT - 4a REGIÃO (RS) - Técnico Judiciário - Tecnologia da
Informação) No ambiente de programação Java:
a) uma classe abstrata permite apenas métodos abstratos.

b) o corpo de um método abstrato termina com ponto e vírgula e a declaração é delimitada por chaves.
c) uma interface pode definir tanto métodos abstratos quanto não abstratos.

d) a herança múltipla permite que mais classes sejam estendidas.

e) toda classe é uma subclasse direta ou indireta da classe Object.

Comentários:

Cada classe, na hierarquia de classes, representa uma camada que adiciona diversas capacidades a um objeto. No topo desta hierarquia você sempre vai encontrar uma classe chamada deObject
(Objeto). Qualquer classe estende implicitamente (sem necessidade de declarar) a classe
Object.
Claro que, na maioria das vezes, isso ocorre indiretamente.

(a) Não, ela permite métodos concretos; (b) Não, não tem chaves; (c) Não, todos os métodos são abstratos; (d) Java não suporta herança múltipla; (e) Perfeito, absolutamente todas as classes são filhas da Classe Object. Gabarito: E
9. (FCC - 2008 - MPE-RS - Técnico em Informática - Área Sistemas) A função Java:
public boolean VerificarCPF (string CPF);

representa um exemplo do conceito de:

a) override.

b) overload.

c) herança.

d) encapsulamento.

e) polimorfismo.

/ 44

/

Comentários:

Essa questão é estranha! Ele não especifica exatamente o que ele quer saber, mas vamos lá: por eliminação! (a) Impossível inferir algo sobre isso; (b) Impossível inferir algo sobre isso; (c) Impossível inferir algo sobre isso; (d) Bem, há um modificador de acesso, portanto representa um exemplo do conceito de encapsulamento; (e) Impossível inferir algo sobre isso. Gabarito: D
1O.(FCC - 2014 - TRT - 16a REGIÃO (MA) - Analista Judiciário - Tecnologia da
Informação)
Considere as classes a seguir, presentes em uma aplicação Java orientada a objetos:

public class Funcionário {
private int id;

private String nome;
private double valorBase;

public Funcionário() {

}

public Funcionário(int id, String nome, double valorBase) {

this.id id;
this.nome nome;

this.valorBase>valorBase;

}

public double getValorBase() {

return valorBase;

}

public double calcularSalario(){

return valorBase;

}

}

public class Mensalista extends Funcionario{
private double descontos;

public Mensalista(double descontos, int id, String nome, double valorBase) {
super(id, nome, valorBase);
this.descontos descontos;

}

«Override public double calcularSalario(){
return super.getValorBase() - descontos;

}

}

public class Diarista extends Funcionário {
private int diasPorSemana;

public Diarista( int diasPorSemana, int id, String nome, double valorBase) {
super(id, nome, valorBase);
this.diasPorSemana « diasPorSemana;

}

©Override public double calcularSalario(){
return super.getValorBase() * diasPorSemana;

}

}

Em uma classe principal foram digitadas, no interior do método main, as seguintes linhas:

double s;
Funcionário f;

f=new Diarista(3,1045Ê,"Ana Maria",90);
s = f.calcularSalario() ;
System.out.println(s) ;

f=new Mensalista(298.5Ê,10457,"Pedro Henrique",877.56);
s = f.calcularSalario();

System.out.println(s) ;

As linhas que contêm a instrução s = f.calcularSalario( ); demonstram um conceito da orientação a objetos conhecido como:
a) encapsulamento.

b) sobrecarga de métodos.

c) polimorfismo.

/

d) sobrescrita de construtores.

e) métodos abstratos.

Comentários:

Primeiro, vamos analisar o código! Saca só... temos três classes: Funcionário,
Mensalista e Diarista.
Observe que as classes Mensalista e Diarista 'estendem' a classe Funcionário, i.e., são filhas deFuncionário! Agora vamos analisar cada classe:

A classe Funcionário possui dois construtores: Funcionário( ) e Funcionário(int id, String nome,double valorBase), além dos métodos getValorBase( ) e calcularSalario( ). Aí você vai me dizer:professor, tem dois construtores? Sim, com mesmo nome e assinaturas diferentes!
Portanto, temos uma: Sobrecarga (Overloading) de Construtores. Bacana?
Já a classe Mensalista possui um construtor Mensalista(double descontos, int id, String nome,double valorBase) e um método calcularSalario(). Opa, perae... esse método é igual ao método da classe Funcionário, concorda? Mesmo nome e mesma assinatura! Portanto, temos umaSobrescrita (ou Override) de métodos.

Por fim, a classe Diarista possui um construtor Diarista(int diasPorSemana, int id, String nome,double valorBase) e um método calcularSalario(). De novo, você vai dizer: professor,
esse método também é igual àquele da classe Funcionário e Mensalista. É verdade, portanto temos umaSobrescrita (ou Override) de métodos.

Agora vamos para o método main! Observe que ele cria uma variável f do tipo
Funcionário. Em seguida, ele cria um objeto Diarista e atribui à variável f. Professor, pode isso?Sim, eu posso atribuir um objeto de uma classe-filha para uma variável do tipo da classe-pai - eu não posso é fazer o contrário (pelo menos, sem um casting). Na linha seguinte, ele diz: s =f.calcularSalario().

Chegamos ao ponto crucial! Ele chama o método calcularSalario( ), mas você lembra que nós temos 3 métodos com esse nome? Temos um na classe-pai e dois nas classes-filhas,sobrescrevendo o método da classe-pai. E qual desses ele está chamando? Lembra que na linha anterior ele diz que f recebe o objeto da classe Diarista? Pois é, portanto, o método calcularSalario(
) é aquele da classe Diarista. Mais abaixo, ele faz exatamente a mesma coisa, mas atribui o objetoMensalistaO à variável f, portanto, na segunda vez que ele chama esse método,
refere-se ao objeto da classe Mensalista. Entendido? Agora vamos para os itens:
(a) Encapsulamento? Não, não tem nenhum modificador de acesso aí;

(b) Sobrecarga de Métodos? Não! Lá em cima, há sobrecarga de construtores. Nessa linha, há sobrescrita de métodos.
(c) Polimorfismo? Perfeito! Nós temos uma sobrescrita de métodos (que é um tipo dePolimorfismo).

(d) Sobrescrita de Construtores? Não! Lá em cima, há sobrecarga de construtores. Nessa linha, há sobrescrita de métodos.
(e) Métodos Abstratos? Não, não há nenhum método abstrato nessa questão.

Aí você vai me dizer: Professor, mas um construtor é um tipo de método!
Logo, se há uma sobrecarga de construtores, há uma sobrecarga de métodos! Sim, concordo contigo! No entanto,temos que lembrar que é uma questão da FCC! Nesse caso, a terceira opção não apresenta problema algum! Já a segunda opção, pode-se dizer que não é exatamente sobrecarga de métodos; é algo mais específico, é uma sobrecarga de construtores. Percebe? Dessa forma, eu
/ 44

/

recomendo não brigar com a banca e marcar a opção que não gera dúvidas.
Agora... se for bastante técnico aqui, você está corretíssimo! A questão possui duas respostas e deveria ser anulada. Gabarito: C
11.(FCC - 2010 - AL-SP - Agente Legislativo de Serviços Técnicos e
Administrativos -
Processamento de Dados) Métodos estáticos em Java são aqueles que:

a) realizam alguma tarefa que é dependente do conteúdo de algum objeto.

b) não podem ser acessados diretamente pelo nome da classe a que pertencem, mas sim por meio de um objeto da classe.
c) realizam alguma tarefa que não é dependente do conteúdo de algum objeto.

d) são acessados por objetos que não necessitam de ser instanciados explicitamente.

e) existem em subclasses de uma herança.

Comentários:

(a) Não, é estático, logo não depende de objetos; (b) Não, é justamente o inverso;
(c) Perfeito,
não depende de objetos! (d) Na verdade, precisam sim ser instanciados explicitamente;
(e) Isso não define um método estático. Gabarito: C
12.(FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da
Informação)
Uma classe Java pode ser instanciada por um comando, cuja sintaxe é:

a) nome_Objeto nome_Classe = new nome_Objeto();

b) nome_Classe nome_Objeto = new nome_Classe();

c) nome_Classe nomejnstancia = new nome_Objeto();

d) nomejnstancia nome_Objeto = new nomeJnstanciaO;

e) nomejnstancia nome_Classe = new nomeJnstanciaO;

Comentários:

/* 1) Operador NEW é responsável por criar um objeto;

* 2) NomeClasseO é o construtor da Classe NomeClasse;

* 3) NomeObjeto é uma variável do Tipo NomeClasse; */

NomeClasse NomeObjeto = new NomeClasseO;

/* Observem que é possível atribuir o objeto de uma

* classe para uma variável de outra classe */

Conforme vimos em aula, trata-se da segunda opção! Gabarito: B

x'"'

/ 44

/

QUESTõES CoMENTADAS - PRoGRAMAçÃo ORIENTADA A

OBJEToS - CEBRASPE

1. (CESPE - 2012 - Banco da Amazônia - Técnico Científico - Análise de Sistemas) Em
Java,
para toda classe, método e variável de instância que se declara há um controle de acesso,independentemente de o controle ser explicitamente indicado.

Comentários:

Conforme vimos em aula, está perfeito! Por que ele diz "independentemente de o controle ser explicitamente indicado"? Porque quando não se indica o modificador de acesso, assume-se que é Pacote ou Default. Gabarito: C
2. (CESPE - 2012 - MPE-PI - Analista Ministerial - Informática - Cargo 6) Em Java,
qualquer método de uma classe pode ser sobrescrito por métodos de outra classe.
Comentários:

//Indica que esse método não possui corpo abstract int soma (int a, int b) {//...//}
//Indica que esse método não pode ser sobrescrito final int soma (int a, int b) {//...//}
//Indica que esse método só pode acessar atributos de classe e não pode ser sobrescrito static int soma (int a, int b) {//...//}
//Indica que esse método foi escrito outra linguagem native int soma (int a, int b) {//...//}
/ 44

/

//Indica que esse método só é executável por uma thread por vez synchronized soma (int a, int b) {//...//}
Não, métodos finais, estáticos e privados não podem ser sobrescritos por métodos de outra classe.
Gabarito: E

3. (CESPE - 2011 - TRE-ES - Técnico - Programação de Sistemas -
Específicos) O
encapsulamento em Java somente pode ser realizado por meio do modificador de acesso protegido.
Comentários:

Não, pode ser Público, Privado, Protegido ou Padrão. Gabarito: E

4. (CESPE - 2009 - ANAC - Analista Administrativo - Tecnologia da Informação) Pelo uso de polimorfismo, uma chamada de método pode fazer que diferentes ações ocorram,dependendo do tipo do objeto que recebe a chamada.

Comentários:

A palavra Polimorfismo vem do grego: muitas formas. Trata-se da capacidade de um objeto poder se comportar de diversas formas dependendo da mensagem recebida. Observem que isso não quer dizer que o objeto fica transformando seu tipo a todo momento. Na verdade, um objeto nasce com um tipo e morre com esse mesmo tipo. O que muda, então? É a forma como nós nos referimos a esse objeto!
Conforme vimos em aula, dependendo do tipo de objeto (se é da Classe-Pai ou da
Classe-Filho),
ações diferentes podem ocorrer. Gabarito: C

5. (CESPE - 2009 - TRT - 17a Região (ES) - Técnico Judiciário - Tecnologia da
Informação) Ao contrário dos tipos primitivos que não são objetos, os tipos de objetos são determinados pela classe de origem.
Comentários:

/ 44

/

Perfeito, perfeito, perfeito! Gabarito: C

6. (CESPE - 2009 - TRT - 17a Região (ES) - Técnico Judiciário - Tecnologia da
Informação)
Uma classe final indica uma classe que não pode ser estendida. Um método final não pode ser redefinido em classes derivadas.
Comentários:

//Indica que esse método não pode ser sobrescrito final int soma (int a, int b) {//...//}
//Essa classe não pode ser estendida final class Carro { //...// }
Conforme vimos em aula, a classe final não pode ter filhos e Método Final não pode ser sobrescrita. Gabarito: C
7. (CESPE - 2008 - TRT - 5a Região (BA) - Técnico Judiciário - Tecnologia da
Informação) Em
Java, os métodos public de uma classe são utilizados pelos clientes da classe para manipular dados armazenados em objetos dessa classe.
Comentários:

Pessoal, esses Modificadores de Acesso determinam quão acessíveis são esses elementos.
Vamos vê-los agora em mais detalhes:
<public>: essa instrução indica que a classe, método ou atributo assim declaradas podem ser acessadas em qualquer lugar e a qualquer momento da execução do programa - é o modificador menos restritivo.
Perfeito, são públicos para toda e qualquer classe. Gabarito: C

/ 44

/

LISTA DE QUESTõES - PRoGRAMAçÃo ORIENTADA A

OBJEToS - MULTIBANCAS

1. (FUNCAB - 2010 - PRODAM-AM - Analista de TI - Desenvolvimento de Sistemas) Seja a seguinte classe Java:
<mod> public class Xpto

{

}

Qual das alternativas a seguir contém um modificador que ao ser usado na declaração acima em substituição ao termo <mod> impedirá que a classe Xpto seja estendida?
a) static b) const c) abstract d) final e) virtual
2. (CESGRANRIO - 2012 - Petrobrás - Técnico de Exploração de Petróleo
Júnior -
Informática) Ao escrever o código da Classe PortaDeCofre em Java para que ela atenda a interface Porta, como um programador deve começar a declaração da classe?
a) public class Porta:PortaDeCofre {

b) public class PortaDeCofre :: Porta {

c) public class PortaDeCofre inherits Porta {

d) public class PortaDeCofre extends Porta {

e) public class PortaDeCofre implements Porta {

3. (ESAF - 2008 - CGU - Tecnologia da Informação) Com relação a essa característica, é correto afirmar que:
a) métodos declarados como public em uma superclasse, quando herdados,
precisam ser protected em todas as subclasses dessa classe.
b) métodos declarados como protected em uma superclasse, quando herdados, precisam ser protected ou public nas subclasses dessa classe.
c) o nível de acesso protected é mais restritivo do que o nível de acesso default.

d) métodos declarados como public só podem ser acessados a partir dos métodos da própria classe ou de classes derivadas.
e) métodos declarados como default só podem ser acessados a partir dos métodos da própria classe.
/ 44

/

4. (FGV - 2015 - PGE/RO - Analista de Sistemas) Na linguagem de programação Java, para indicar que uma classe A é derivada de B, utiliza-se, na declaração de A, o modificador:
a) imports;

b) extends;

c) inherits;

d) subclass;

e) superclass.

5. (FGV- 2014 - TJ/GO - Analista de Sistemas) Se uma classe na linguagem Java é declarada com o modificador abstract, então essa classe:
a) não pode ser referenciada;

b) não pode ser estendida;

c) não pode ser instanciada;

d) pode ser instanciada apenas uma vez;

e) não pode possuir métodos estáticos.

6. (FGV - 2014 - TJ/GO - Analista de Sistemas) Na linguagem de programação Java, uma classe declarada com o modificador final:
a) não pode ser instanciada;

b) não pode ser estendida;

c) pode ter o modificador abstract também presente na declaração;

d) não pode ter métodos estáticos;

e) não pode ter métodos de instância.

7. (FGV - 2015 - TJ/BA - Analista de Sistemas) Em Java, os métodos declarados sem modificadores em uma interface são implicitamente:
a) públicos e estáticos;

b) públicos e abstratos;

c) privados e estáticos;

d) públicos e finais;

e) privados e abstratos.

/ 44

/

GABARITo

GABARITO

1. D

2. E

3. B

4. B

5. C

6. B

7. B

,

LISTA DE QUESTõES - PRoGRAMAçÃo ORIENTADA A

OBJEToS - FCC

1. (FCC - 2009 - TJ-SE - Técnico Judiciário - Programação de Sistemas) Um objeto é instanciado em Java por meio do operador:
a) instanceof.

b) extend.

c) new.

d) this.

e) type.

2. (FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da Informação)
Uma classe Java pode ser instanciada por um comando, cuja sintaxe é:

a) nome_Objeto nome_Classe = new nome_Objeto();

b) nome_Classe nome_Objeto = new nome_Classe();

c) nome_Classe nomejnstancia = new nome_Objeto();

d) nomejnstancia nome_Objeto = new nomejnstancia();

e) nomejnstancia nome_Classe = new nomeJnstanciaQ;

3. (FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da Informação) A
diretiva public é utilizada em Java para aplicar a encapsulação pública:

a) aos métodos e classes, apenas.

b) aos atributos, métodos e classes.

c) às classes, apenas.

d) aos atributos, apenas.

e) aos atributos e classes, apenas.

4. (FCC - 2008 - TCE-AL - Programador) Em Java, para alterar a visibilidade do elemento em que se aplica, entre outros, utiliza-se o modificador de acesso:
a) static.

b) abstract.

c) protected.

d) volatile.

e) transient.

/ 44

/

5. (FCC - 2005 - TRE-MG - Técnico Judiciário - Programação de Sistemas) Os métodos Java que não retornam valores devem possuir no parâmetro tipo-de-retorno a palavra:
a) static.

b) public.

c) void.

d) main.

e) string args.

6. (FCC - 2012 - MPE-AP - Analista Ministerial - Tecnologia da Informação) Analise o código das classes a seguir presentes em um mesmo pacote de um projeto Java:
public class NewClassA {

public double calcular(int x, int y) {
return x + y;

}

public double calcular(double x, double y) {
return x* y;

}

}

public class NewClassB extends NewClassA {

}

public class Start {

public static void main(String[] args) {

Com base nos códigos apresentados e nos conceitos da orientação a objetos é correto afirmar:
a) No método main da classe Start não é possível instanciar objetos das classes
NewClassA e
NewClassB, pois essas classes não contêm um construtor válido.

/ 44

/

b) Se for digitada a instrução NewClassB c = new NewClassA(); no método main da classe Start será instanciado um objeto da NewClassA.
c) Se for digitada a instrução NewClassA b = new NewClassB(); no método main da classe Start ocorrerá um erro, pois não é possível criar um objeto da NewClassA por meio do construtor daNewClassB.

d) A existência de dois métodos de mesmo nome na NewClassA que recebem a mesma quantidade de parâmetros indica que está ocorrendo uma sobrescrita de métodos.
e) Por meio de um objeto da NewClassB será possível acessar os métodos presentes naNewClassA.

7. (FCC - 2012 - TRE-CE - Técnico Judiciário - Programação de Sistemas) Com relação a herança na programação orientada a objetos com Java, é INCORRETO afirmar:
a) Uma subclasse herda os métodos da superclasse, entretanto, pode ter seus próprios métodos.
b) Quando se instancia um objeto da subclasse, podem ser passados valores para os atributos da superclasse.
c) Um objeto da subclasse pode ser um objeto da superclasse.

d) Em uma superclasse, para acessar métodos da subclasse deve ser usada a instrução super.

e) Para definir que a subclasse herda as características da superclasse utiliza-se a instrução extends na declaração da subclasse.
8. (FCC - 2011 - TRT - 4a REGIÃO (RS) - Técnico Judiciário - Tecnologia da Informação) No ambiente de programação Java:
a) uma classe abstrata permite apenas métodos abstratos.

b) o corpo de um método abstrato termina com ponto e vírgula e a declaração é delimitada por chaves.
c) uma interface pode definir tanto métodos abstratos quanto não abstratos.

d) a herança múltipla permite que mais classes sejam estendidas.

e) toda classe é uma subclasse direta ou indireta da classe Object.

9. (FCC - 2008 - MPE-RS - Técnico em Informática - Área Sistemas) A função Java:

public boolean VerificarCPF (string CPF);

representa um exemplo do conceito de:

a) override.

b) overload.

c) herança.

/ 44

/

d) encapsulamento.

e) polimorfismo.

1O.(FCC - 2014 - TRT - 16a REGIÃO (MA) - Analista Judiciário - Tecnologia da Informação)
Considere as classes a seguir, presentes em uma aplicação Java orientada a objetos:

public class Funcionário {
private int id;

private String nome;
private double valorBase;

public Funcionário() {

}

public Funcionário(int id, String nome, double valorBase) {

this.id « id;
this.nome nome;

this.valorBase«valorBase;

}

public double getValorBase() {

retum valorBase;

}

public double calcularSalario(){

return valorBase;

}

}

public class Mensalista extends Funcionario{
private double descontos;

public Mensalista(double descontos, int id, String nome, double valorBase) {
super(id, nome, valorBase);
this.descontos descontos;

}

«Override public double calcularSalario(){
retum super.getValorBase () - descontos;

}

}

public class Diarista extends Funcionário {
private int diasPorSemana;

public Diarista( int diasPorSemana, int id, String nome, double valorBase) {
super(id, nome, valorBase);
this.diasPorSemana « diasPorSemana;

}

©Override public double calcularSalario(){
retum super.getValorBase () * diasPorSemana;

}

}

Em uma classe principal foram digitadas, no interior do método main, as seguintes linhas:

double s;
Funcionário f;

f=new Diarista(3,10456,"Ana Maria",90);
s = f.calcularSalario();
System.out.println(s);

f=new Mensal ist a (298. SÊ, 104 57,11 Pedro Henrique",877.56);
s = f.calcularSalario();

System.out.println(s);

As linhas que contêm a instrução s = f.calcularSalario( ); demonstram um conceito da orientação a objetos conhecido como:
a) encapsulamento.

b) sobrecarga de métodos.

c) polimorfismo.

d) sobrescrita de construtores.

e) métodos abstratos.

11. (FCC - 2010 - AL-SP - Agente Legislativo de Serviços Técnicos e Administrativos -
Processamento de Dados) Métodos estáticos em Java são aqueles que:

a) realizam alguma tarefa que é dependente do conteúdo de algum objeto.

b) não podem ser acessados diretamente pelo nome da classe a que pertencem, mas sim por meio de um objeto da classe.
c) realizam alguma tarefa que não é dependente do conteúdo de algum objeto.

d) são acessados por objetos que não necessitam de ser instanciados explicitamente.

e) existem em subclasses de uma herança.

12. (FCC - 2009 - TRT - 16a REGIÃO (MA) - Técnico Judiciário - Tecnologia da Informação)
Uma classe Java pode ser instanciada por um comando, cuja sintaxe é:

a) nome_Objeto nome_Classe = new nome_Objeto();

b) nome_Classe nome_Objeto = new nome_Classe();

c) nome_Classe nomejnstancia = new nome_Objeto();

d) nomejnstancia nome_Objeto = new nomejnstancia();

e) nomejnstancia nome_Classe = new nomejnstancia();

, 44

GABARITo

GABARITO

1. c

2. B

3. B

4. C

5. C

6. E

7. D

8. E

9. D

10. C

11. C

12. B

,

/

LISTA DE QUESTõES - PRoGRAMAçÃo ORIENTADA A

OBJEToS - CEBRASPE

1. (CESPE - 2012 - Banco da Amazônia - Técnico Científico - Análise de Sistemas)
Em Java,
para toda classe, método e variável de instância que se declara há um controle de acesso,independentemente de o controle ser explicitamente indicado.

2. (CESPE - 2012 - MPE-PI - Analista Ministerial - Informática - Cargo 6) Em Java,
qualquer método de uma classe pode ser sobrescrito por métodos de outra classe.
3. (CESPE - 2011 - TRE-ES - Técnico - Programação de Sistemas
- Específicos) O
encapsulamento em Java somente pode ser realizado por meio do modificador de acesso protegido.
4. (CESPE - 2009 - ANAC - Analista Administrativo - Tecnologia da Informação) Pelo uso de polimorfismo, uma chamada de método pode fazer que diferentes ações ocorram,dependendo do tipo do objeto que recebe a chamada.

5. (CESPE - 2009 - TRT - 17a Região (ES) - Técnico Judiciário - Tecnologia da
Informação) Ao contrário dos tipos primitivos que não são objetos, os tipos de objetos são determinados pela classe de origem.
6. (CESPE - 2009 - TRT - 17a Região (ES) - Técnico Judiciário - Tecnologia da
Informação)
Uma classe final indica uma classe que não pode ser estendida. Um método final não pode ser redefinido em classes derivadas.
7. (CESPE - 2008 - TRT - 5a Região (BA) - Técnico Judiciário - Tecnologia da
Informação) Em
Java, os métodos public de uma classe são utilizados pelos clientes da classe para manipular dados armazenados em objetos dessa classe.
GABARITo

/

