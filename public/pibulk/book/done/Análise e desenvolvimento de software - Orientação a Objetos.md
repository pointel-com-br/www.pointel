# Análise e desenvolvimento de software - Orientação a Objetos

A orientação a objetos é um paradigma de programação que organiza o código em torno de objetos, que são instâncias de classes. Ela se baseia em quatro princípios fundamentais: encapsulamento, herança, polimorfismo e abstração.

1. Encapsulamento: É o princípio que define a restrição de acesso direto aos dados de um objeto e a necessidade de utilizar métodos (funções) para manipulá-los. Isso significa que os dados internos de um objeto são protegidos e só podem ser acessados ou modificados através de métodos específicos. O encapsulamento ajuda a garantir a integridade dos dados e evita a dependência direta entre diferentes partes do código.

2. Herança: É um mecanismo que permite que uma classe herde características (atributos e métodos) de outra classe, estabelecendo uma relação de especialização. A classe que herda é chamada de classe derivada ou subclasse, e a classe que é herdada é chamada de classe base ou superclasse. A herança permite reutilizar o código existente, promovendo a modularidade e a extensibilidade do sistema.

3. Polimorfismo: É a capacidade de um objeto se comportar de diferentes formas, dependendo do contexto em que é utilizado. O polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme através de uma interface comum. Isso facilita a substituição de objetos em tempo de execução e possibilita o desenvolvimento de código mais flexível e extensível.

4. Abstração: É o processo de identificar as características essenciais de um objeto ou conceito e modelá-las em uma classe. A abstração permite simplificar a complexidade do sistema, concentrando-se apenas nos aspectos relevantes e ocultando detalhes desnecessários. As classes abstratas fornecem uma base para a criação de objetos concretos.

A orientação a objetos oferece vários benefícios no desenvolvimento de software, incluindo:

- Reutilização de código: Através da herança e do polimorfismo, é possível aproveitar o código existente em novas classes, evitando duplicação e melhorando a produtividade.

- Modularidade: A organização do código em classes e objetos facilita a divisão do sistema em partes independentes e interconectadas. Cada classe é responsável por uma funcionalidade específica, tornando o sistema mais fácil de entender, manter e testar.

- Flexibilidade e extensibilidade: Através do polimorfismo e da abstração, é possível adicionar novas funcionalidades ao sistema sem alterar o código existente. Isso permite que o sistema seja adaptado e evoluído de forma mais eficiente.

- Facilidade de manutenção: O encapsulamento e a separação de responsabilidades entre as classes tornam as alterações e correções de bugs mais localizadas, reduzindo o impacto em outras partes do sistema.

A orientação a objetos é amplamente utilizada em diversas linguagens de programação, como Java, C++, C#, Python, entre outras. Dominar os conceitos e princípios da orientação a objetos é essencial para desenvolver sistemas robustos, flexíveis e de qualidade.

A Orientação a Objetos tem alguns pilares que devem ser implementados em qualquer linguagem de programação. Muitas linguagens procedurais possuem caraterísticas semelhantes à orientação a objetos, como a similaridade dos registros em C com classes, mas isso não basta que algumas dessas características estejam presentes para ser considerada uma linguagem orientada a objetos! Professor, e quais são esses pilares?? Padawan, nunca se esqueça, uma linguagem de programação só pode ser chamada de OO se tiver suporte nativo a: Encapsulamento, Herança, Composição e Polimorfismo. Alguns autores afirmar que as quatro caraterística na verdade são somente uma: o princípio da abstração.

Índice

1 Classe

1.1 Objetos

1.2 Atributos

1.3 Métodos

2 Interface

3 Encapsulamento

4 Polimorfismo

5 Herança

Classe

A classe é a planta ou esquema que indica como os objetos são criados, quais os seus comportamentos e variáveis de estado. Para declarar uma classe, é necessário utilizar a sintaxe a seguir:

[palavra-chave] class NomeDaClasse {
// Atributos e Métodos
}

Portanto para declarar uma classe, deve-se colocar a palavra class seguida de um identificador que irá servir de nome para a classe. O identificador pode ser qualquer palavra, exceto palavras reservadas. Por exemplo: class Conta introduz a declaração de uma nova classe chamada Conta. Note que, por convenção, o nome de uma classe inicia sempre com uma letra maiúscula. A Palavra- Chave é opcional, podendo ser:

// Essa classe pode ser acessada por todos public class Carro { ... }
// Essa classe não pode gerar instâncias abstract class Carro { ... }
// Essa classe não pode ser estendida final class Carro {...}
Objetos

Um objeto é uma instância de uma classe. Para criar um objeto, devemos utilizar a seguinte sintaxe:

new construtor();

O comando new, também conhecido como operador de criação, cria um novo objeto, alocando memória para o objeto e inicializando essa memória para valores default. Ele necessita de um operando: o construtor, que é o nome de um método especial que constrói o objeto. Uma vez construído, o objeto deve ser atribuído a uma variável, para que possa ser utilizado e referenciado no futuro.

A linguagem Java assume a responsabilidade de destruir qualquer objeto criado que não esteja sendo usando. Para tal, utiliza um Coletor de Lixo (Garbage Collector), que é executado em intervalos regulares, examinando cada objeto para ver se ele ainda é referenciado por alguma variável. Caso o objeto não seja utilizado ao menos por uma variável, ele é destruído e sua memória é liberada.

Atributos

Um atributo ou campo é uma variável declarada no corpo de uma classe. Ele serve para armazenar o estado de um objeto (atributo de instância) ou o estado de uma classe (atributo de classe). A sintaxe de declaração de um atributo é a seguinte:

[palavra-chave] tipoAtributo NomeAtributo [ = expressão ] ;

A Palavra-Chave é opcional, podendo ser: Final, Volatile, Static ou Transient.

class Empregado {

final String Nome ; // Indica que Nome é um atributo constante;

volatile Salario ; // Indica que Salário é modificável por threads distintas;

static Idade ; // Indica que Idade é compartilhada por todos objetos;

transient Sexo ; // Indica que Sexo não pode ser serializável;

}

Modificadores de Acesso:

class Empregado {

public String nome ; // Nome: público private int Salario ; // Salário: privado protected short Idade ; // Idade: protegido char Sexo ; // Sexo: default
}

Métodos

Java utiliza métodos para se referir a trechos de código que são associados a classes. Se os atributos servem para manter ou armazenar o estado ou o valor de um objeto, os métodos servem para descrever os comportamentos de um objeto ou classe. Um método é muito similar a uma função em C. A maior diferença é que os métodos da linguagem Java são declarados completamente dentro de uma classe.

[Palavras-Chave] TipoRetorno NomeMetodo ( [Lista de Parâmetros] ) {

// Corpo do Método

}

A sintaxe de declaração de um método é apresentada acima. A Palavra-Chave é opcional, podendo ser: Abstract, Final, Static, Native e Synchronized.

// Indica que esse método não possui corpo abstract int soma ( int a , int b ) { ... }
// Indica que esse método não pode ser sobrescrito final int soma ( int a , int b ) { ... }
// Indica que esse método só pode acessar atributos de classe e não pode ser sobrescrito static int soma ( int a , int b ) { ... }
// Indica que esse método foi escrito outra linguagem native int soma ( int a , int b ) { ... }
// Indica que esse método só é executável por uma thread por vez synchronized soma ( int a , int b ) { ... }
Modificadores de Acesso:

public int soma ( int a , int b ) { ... }

private int soma ( int a, int b ) { ... }

protected int soma ( int a , int b ) { ... }

int soma ( int a , int b ) { ... }

Vamos falar agora sobre um método importante: Construtor! Ele é um método especial, chamado pelo operador new quando um novo objeto necessita ser criado. Dentro do construtor, pode-se colocar código customizado de inicialização do objeto. Em geral, ele deve ter o mesmo nome da classe em que for declarado. Além disso, um construtor não deve ter um tipo de retorno em sua declaração.

Professor, não entendo uma coisa! Em geral, no código da classe não há nenhum método com o nome do método construtor. Ora, não há declaração de método algum! Como é isso? É verdade! Basicamente, quando você não declara um construtor para uma classe, o compilador cria um construtor padrão com uma lista vazia de parâmetros.

Pode-se criar diversos construtores para uma mesma classe.
Outro método muito importante é o Método Main! Pois é, ele é sempre definido como um método de classe, i.e., possui um modificador static:

public static void main ( String [ ] args ) throws java . lang . Exception

Interface

Galera, o que é uma Interface? É simplesmente um contrato! Quando vocês assinam o contrato do seguro de um carro, vocês estão se comprometendo a atender aquilo que lá está escrito. Analogamente, a interface é um contrato que obriga aqueles que a assinam a implementar os métodos lá presentes. Elas ajudam a padronizar implementações - entradas e saídas.

Em outras palavras, é um recurso utilizado em Java para obrigar a um determinado grupo de classes a ter métodos ou propriedades em comum para existir em um determinado contexto, contudo os métodos podem ser implementados em cada classe de uma maneira diferente. Em geral, as interfaces são compostas basicamente de um conjunto de assinaturas de métodos públicos e abstratos.

public interface FiguraGeometrica {

public String getNomeFigura ( ) ;

public int getArea ( int vertice ) ;

public int getPerimetro ( ) ;

}

A sintaxe para implementar uma Interface utiliza a palavra reservada implements:

public class ClasseImplementadoraDeInterfaces implements FiguraGeometrica

Professor, qual a diferença entre uma Interface e uma Classe Abstrata? Bem, Interfaces não são classes; são, na verdade, entidades que não possuem qualquer implementação, apenas assinatura, sendo que todos os seus métodos são públicos e abstratos. Já as Classes Abstratas também contêm, em geral, métodos abstratos (sem corpo), mas podem ter vários métodos concretos.

Uma Classe Abstrata pode, inclusive, não conter nenhum método abstrato, i.e., todos os seus métodos são concretos. No entanto, se uma classe tiver um único método abstrato que seja, ela será considerada uma Classe Abstrata. Aliás, uma Interface é também chamada de classe abstrata pura por conta disso, ou seja, não há impurezas (isto é, métodos concretos).

Encapsulamento

Pessoal, nós já sabemos que para se descobrir o que um objeto pode fazer, basta olhar para as assinaturas de seus métodos públicos definidos na classe desse objeto - que formam uma interface de uso. A assinatura de um método é composta pelo seu nome e seus parâmetros. Por outro lado, para descobrir como um objeto realiza suas operações, deve-se observar o corpo de cada um dos métodos da classe.

Os corpos dos métodos constituem a implementação das operações dos objetos. Professor, por que nós encapsulamentos classes, atributos e métodos? Cara, por duas razões: desenvolvimento e manutenibilidade. O encapsulamento ajuda a aumentar a divisão de responsabilidades (ou coesão) e, dessa forma, fica mais fácil e rápido desenvolver sistemas em módulos.

Da mesma forma, ele ajuda a manutenção, visto que para torna-se mais difícil fazer "besteiras" no código e atrapalhar manutenções futuras. Trazendo isso para a vida real, lidamos com encapsulamento o tempo inteiro. Você sabe como usar um controle remoto, mas você não sabe como ele funciona internamente. Encapsula-se seu funcionamento interno e disponibiliza-se apenas sua interface ao usuário.

Chegamos ao conceito de Modificadores de Acesso! Eles são utilizados para modificar o modo como classes, métodos e variáveis são acessadas. Existem três modificadores de acesso e um quarto nível (acesso default/friendly), quando não se usa nenhum dos modificadores citados. Toda classe, método e variáveis de instância declaradas possuem um controle de acesso.

Pessoal, esses Modificadores de Acesso determinam quão acessíveis são esses elementos. Vamos vê-los agora em mais detalhes:

§ public : essa instrução indica que a classe, método ou atributo assim declaradas podem ser acessadas em qualquer lugar e a qualquer momento da execução do programa - é o modificador menos restritivo.

§ private : essa instrução indica que métodos ou atributos (classes, não) assim declaradas podem ser acessadas apenas dentro da classe que os criou. Subclasses herdam-nos, mas não os acessam - é o modificador mais restritivo1.

§ protected : essa instrução indica que métodos ou atributos (classes, não) assim declaradas somente podem ser acessadas dentro do pacote em que está contida ou por subclasses no mesmo pacote.

§ default : também chamado friendly, não há palavra para esse modificador porque ele é, na verdade, a ausência de um modificador. Indica-se que a classe, método ou atributo podem ser acessadas por classes do mesmo pacote.

Especificador

Privado ( - )

Própria Classe

Sim

Subclasse

Não

Pacote

Não

Global

Não

Especificador

<Vazio> ( ~ )

Própria Classe

Sim

Subclasse

Não (quando não estiver no mesmo pacote)

Pacote

Sim

Global

Não

Especificador

Protegido ( # )

Própria Classe

Sim

Subclasse

Sim

Pacote

Sim

Global

Não

Especificador

Público ( + )

Própria Classe

Sim

Subclasse

Sim

Pacote

Sim

Global

Sim

É importante ressaltar que, em caso de não haver modificador, a subclasse pode ou não acessar os métodos e atributos da sua superclasse, e isso depende da localização da subclasse. Se ela estiver em um pacote diferente do pacote da superclasse, não poderá acessar. Se estiver em um mesmo pacote da superclasse, poderá acessar. Logo, para diferenciar o Modificador Pacote do Modificador Protegido, deve-se saber primeiramente se é desejável que a subclasse possa ter acesso a atributos e métodos da classe.

Pensem comigo! Acessar ou editar propriedades de objetos, manipulando-as diretamente, pode ser muito perigoso e gerar muitos problemas. Por conta disso, é mais seguro, para a integridade dos objetos e, consequentemente, para a integridade da aplicação, que esse acesso ou edição sejam realizados através de métodos desse objeto.

Utilizando métodos, podemos controlar como consultas e modificações são realizadas, controlando-as. Para tal, podemos utilizar Métodos Getters e Setters - para recuperar dados e inserir dados, respectivamente. Para o primeiro, utiliza-se o Método Get; para o segundo, utiliza- se o Método Set. Em geral, costuma-se declarar atributos como privados, e métodos e classes como públicos.

Polimorfismo

A palavra Polimorfismo vem do grego: muitas formas. Trata-se da capacidade de um objeto poder se comportar de diversas formas dependendo da mensagem recebida. Observem que isso não quer dizer que o objeto fica transformando seu tipo a todo momento. Na verdade, um objeto nasce com um tipo e morre com esse mesmo tipo. O que muda, então? É a forma como nós nos referimos a esse objeto!

Existem dois tipos de polimorfismo:

§ Polimorfismo Estático: ocorre quando uma classe possui métodos com mesmo nome, entretanto assinaturas diferentes, i.e., métodos de uma mesma classe se sobrecarregando. Pode ser chamada também de Sobrecarga ou Overloading. Ocorre em Tempo de Compilação e alguns não o consideram um tipo de polimorfismo, porque a assinatura é diferente.

§ Polimorfismo Dinâmico: ocorre quando uma classe possui um método com mesmo nome e mesma assinatura que um método de sua superclasse, i.e., o método da classe-filha sobrescreve o método da classe-pai. Pode ser chamada também de Sobrescrita, Overriding, Redefinição ou Sobreposição. Ocorre em Tempo de Execução e é um corolário do conceito de herança.
Professor, o que você quer dizer com mesma assinatura e assinatura diferente? É a mesma quantidade, tipo e ordem dos parâmetros. Em outras palavras:

// Assinatura Igual: quantidade, tipo e ordem public String EntendendoAssinatura ( int A , char B ) ;
public String EntendendoAssinatura ( int C , char D ) ;

// Assinatura Diferente: quantidade diferente public String EntendendoAssinatura ( long A , long B , long C ) ;
public String EntendendoAssinatura ( long A , long B ) ;

// Assinatura Diferente: tipo diferente public String EntendendoAssinatura ( long A , long B ) ;
public String EntendendoAssinatura ( char A , long B ) ;

// Assinatura Diferente: ordem diferente public String EntendendoAssinatura ( int A , char B ) ;
public String EntendendoAssinatura ( char B , int A ) ;

Agora vamos ver um exemplo de Polimorfismo Dinâmico. Eu pensei comigo mesmo: O que seria uma característica comum de praticamente todos os animais? Emitir sons! Observem que eu criei uma classe abstrata que possui um único método - também abstrato -, que não retorna valor algum e não recebe nenhum argumento. Vejam a classe abaixo:

abstract class Animal {

abstract void som ( ) ;

}

Dito isso, vou criar dois animais do meu gosto pessoal: um gato e um cachorro! Bem, o gato é um animal! Que relacionamento é esse "é um"? Herança! Portanto as classes gato e cachorro serão classes filhas da superclasse Animal. Observem abaixo que ambas implementam o método abstract void som( ), porém cada uma a sua maneira, visto que gatos e cachorros emitem sons diferentes!

class Gato extends Animal {

void som ( ) {

System . out . println ( " MIAU! " ) ;

}

}

class Cachorro extends Animal {

void som ( ) {

System . out . println ( " AUAU! " ) ;

}

}

Pois bem! Vamos ver agora o Polimorfismo Dinâmico em ação. Criaremos um objeto do tipo Gato e atribuiremos a um objeto do tipo Animal. Professor, você pode fazer isso? Sim, porque Gato é filho de Animal - é similar a um casting implícito! Em seguida chamaremos o método som(). Por fim, faremos o mesmo procedimento com o objeto do tipo Cachorro.

public static void main ( String [ ] args ) {

Animal animal = new Gato ( ) ;

animal . som ( ) ; // Emite o som MIAU!

Animal animal = new Cachorro ( ) ;

animal . som ( ) ; // Emite o som AUAU!

}

Olha que bacana: existem dois métodos com exatamente o mesmo nome e mesma assinatura! Como o compilador saberá qual deve ser chamado? Ele não saberá - tem que ser em tempo de execução. No primeiro momento, ele apresentará "MIAU!", porque animal é nesse instante um gato. Depois fazemos outra atribuição e ele apresentará "AUAU", porque animal naquele instante é um cachorro.

O Polimorfismo Estático é bem mais simples! Imaginem que eu deseje fazer dois cálculos matemáticos. Primeiro somar três números e depois somar apenas dois números. Eu posso ter dois métodos com mesmo nome, mas assinaturas diferentes. Dessa forma, se eu passar três valores, ele saberá que é um método; e se eu passar dois valores, ele saberá que é outro método. Simples, não?

Atributos com o mesmo nome na classe/subclasse substituem os herdados. Ademais, métodos declarados com a palavra-reservada final não podem ser redefinidos. Já os métodos abstratos devem ser redefinidos na subclasse ou declarados como abstratos para que sejam implementados pela classe-neta. Por fim, membros definidos na superclasse podem ser acessados na subclasse.

Herança

Herança é a habilidade de se derivar alguma coisa específica a partir de algo mais genérico. Nós encontramos essa habilidade ou capacidade diversas vezes em nosso cotidiano. Por exemplo: um Pálio estacionado na garagem do seu vizinho é uma instância específica da categoria Carro, mais genérica. Da mesma forma, uma Honda CG 125 é uma instância específica da categoria mais genérica Moto.

Se levarmos as categorias Carro e Moto para um outro nível mais elevado, as duas se relacionarão uma com a outra por serem instâncias específicas de uma categoria mais genérica ainda que elas: a categoria Veículo. Em outras palavras, carros e motos são veículos. A imagem abaixo esquematiza as relações entre Pálio, Carro, Honda CG 125, Moto e Veículo.

Esse exemplo ilustrou a Herança Simples! Neste caso, uma entidade herda estados e comportamentos (atributos e métodos) de uma e somente uma categoria. O Pálio, por exemplo, herda da categoria Carro (e somente dela, diretamente). Em contraste, a Herança Múltipla permite que uma entidade herde diretamente comportamentos e estados de duas ou mais categorias ao mesmo tempo.

Imagine um Empregado chamado José de uma empresa qualquer. Para ser mais específico, pense em José como sendo tanto Gerente quanto Contador simultaneamente dessa empresa. Ele herdaria as capacidades de um Gerente e de um Contador, concordam? Portanto, em uma hierarquia de entidades, João herdaria de duas classes diferentes diretamente, como apresenta a imagem abaixo:

A sintaxe da herança sugere que você pode estender uma e somente uma classe. O Java não suporta Herança Múltipla, porque - segundo projetistas da linguagem - esse tipo de implementação poderia gerar confusão. Imagine, por exemplo, duas classes-base declarando um atributo que possua o mesmo nome, mas com tipos diferentes. Qual dos dois a classe-filha deveria herdar?

A mesma situação poderia acontecer com um método! Se dois métodos possuíssem o mesmo nome, mas diferentes listas de parâmetros ou tipos de retorno, qual deles a subclasse deveria herdar? Vocês percebem como isso poderia causar inconsistências de projeto? Para prevenir tais problemas, a linguagem Java rejeita a implementação de herança múltipla.

Novas classes derivam capacidades (expressas como atributos e métodos) de classes já existentes. Isso faz com que o tempo de desenvolvimento de uma aplicação seja bem menor, pois classes já existentes e comprovadamente funcionais (livres de erros e já testadas) são reaproveitadas (ou reutilizadas). A sintaxe que expressa o conceito de extensão de classes é a seguinte:

class NomeClasseFilha extends NomeClassePai {

// Atributos e Métodos

}

Essa sintaxe pode ser lida da seguinte forma: NomeClasseFilha estende NomeClassePai. Em outras palavras, NomeClasseFilha herda (ou deriva) capacidades (expressas através de atributos e métodos) de NomeClassePai. A NomeClasseFilha é conhecida como subclasse, classe derivada ou classe-filha e NomeClassePai é conhecida como superclasse, classe-base ou classe-pai.

A palavra-chave extends faz com que uma subclasse herde (receba) todos os atributos e métodos declarados na classe-pai (desde que ela não seja final), incluindo todas as classes-pai da classe-pai. A classe-filha pode acessar todos os atributos e métodos não-privados. Ela herda, mas não acessa (ao menos diretamente) métodos e atributos privados.

Todo objeto criado a partir de uma subclasse é também um objeto do tipo da sua superclasse (Ex: um objeto do tipo Carro também é um objeto do tipo Veículo). Essa afirmação implica o fato de que você pode atribuir um objeto de uma subclasse para uma referência criada ou declarada para um objeto de sua superclasse. Como assim, professor? Vejamos!

// Objeto do tipo Carro é um objeto do tipo Veículo

Veiculo v = new Carro ( ) ;

A linha de código acima cria um objeto do tipo Carro e atribui sua referência à variável v. Note que essa variável v é uma variável que armazena referências para objetos do tipo Veículo. Esse tipo de atribuição é perfeitamente possível, já que um Carro é uma subclasse de Veículo. Através da variável v, é possível chamar os métodos que pertencem ao tipo Veículo.

Portanto, pode-se utilizar esse artifício de nomeação para transformar uma classe-filha em qualquer uma de suas classes-pai. Professor, é possível fazer o inverso? Pode-se atribuir uma classe-pai a uma classe-filha? Não, isso só pode ser feito por meio de um type cast. Assim, uma variável pode assumir momentaneamente outro tipo para que o programador possa utilizá-la.
