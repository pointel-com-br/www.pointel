# Bizu Estratégico - Desenvolvimento de Software

Olá, prezado aluno. Tudo certo?

Neste material, traremos uma seleção de bizus da disciplina de Desenvolvimento de software para o concurso de Analista - Especialidade: Tecnologia.
O objetivo é proporcionar uma revisão rápida e de alta qualidade aos alunos por meio de tópicos que possuem as maiores chances de incidência em prova.
Todos os bizus destinam-se a alunos que já estejam na fase bem final de revisão (que já estudaram bastante o conteúdo teórico da disciplina e, nos últimos dias, precisam revisar por algum material bem curto e objetivo).
Além disso, utilizamos os materiais do professor para elaborar esse
Apresentação

Antes de começarmos, gostaria de me apresentar. Meu nome é
Elizabeth Menezes, tenho 32 anos e sou natural do Pernambuco. Sou graduada em Administração pela UFPE e Pós-Graduada em DireitoAdministrativo e Constitucional.

Atualmente, exerço o cargo de Auditora de Controle Externo no
Tribunal de Contas do Estado de São Paulo (TCE-SP). Também fui aprovada e nomeada para outros concursos da área fiscal (Auditor FiscalEstadual e Municipal) e da área de controle.

Serei a responsável pelo Bizu Estratégico de Desenvolvimento de software e, com ele, pretendo abordar os tópicos mais cobrados nessa disciplina, de maneira concisa e objetiva, por meio de uma linguagem bem clara!
Espero que gostem!

Um grande abraço e bons estudos!

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

ANÁLISE ESTATÍSTICA

Pessoal, segue abaixo uma análise estatística dos assuntos mais exigidos no âmbito da disciplina deDesenvolvimento de software:

Com essa análise, podemos verificar quais são os temas mais exigidos e, através disso,
focaremos nos principais pontos em nossa revisão!
Desenvolvimento de software - SERPRO

Assunto Bizu

Linguagens de programação. Java 1

Caderno de Questões http://questo.es/lqv6nc
PHP

Tecnologias e práticas frontend web: HTML

2 http://questo.es/uazuuh

3 http://questo.es/bcl7u8

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

Desenvolvimento de software

1. Linguagens de programação. Java

Java

* O Java é a principal linguagem de programação e plataforma de desenvolvimento. Reduz custos e prazos de desenvolvimento, impulsiona a inovação e aprimora os serviços de aplicativos. Com milhões de desenvolvedores executando mais de 51 bilhões de Java Virtual Machines em todo o mundo.
CARACTERÍSTICA | DESCRIÇÃO

Não contém redundâncias e é fácil de entender, implementar e usar. Parecida com

CONCISA E SIMPLES

C++ para facilitar compreensão por grande parte de programadores. É uma evolução de C++: não suporta aritmética de ponteiros, registros, coerdons, etc.
ORIENTADA A OBJETOS Suporta os principais conceitos de orientação a objetos. Favorece reusabilidade.
Altamente tipada. Programas são confiáveis. Reduz imprevistos em tempo de

ROBUSTA

execução: variáveis são automaticamente inicializadas, uso disciplinado de ponteiros, rotinas devem ser chamadas corretamente, etc.
PORTÁVEL Completamente especificada. Não contém aspectos dependentes da implementação: o tamanho dos tipos é fixo para qualquer implementação, etc.
SEGURA Restrições de acesso a arquivos, manipulação de ponteiros, etc. Implica que não é útil para desenvolver certas aplicações como device drivers*.
CONCORRENTE Suporta aplicações concorrentes: multithreads, monitores, execução atômica.

INDEPENDENTE DE
PLATAFORMA

Geração de bytecode que pode ser interpretado para qualquer arquitetura e sistema operacional tendo o sistema Java. Facilita distribuição de software.
INTERPRETADA Facilita desenvolvimento exploratório.

COMPILADA Utilizando compiladores, bytecodes podem ser traduzidos em tempo de execução para código de máquina.
Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

JAVA SE

PLATAFORMA CENTRAL DE
PROGRAMAÇÃOJAVA

* CONTÉM TODAS AS
BIBLIOTECAS EAPIS

OPENJDK: IMPLEMENTAÇÃO
GRATUITA E DE CÓDIGO
ABERTO DO JAVA SE.

* APLICATIVOS COMJRE
INSTALADO PODEM
EXECUTAR EM VÁRIOS
SISTEMAS OPERACIONAIS

JAVA EE

PDLISAPTOANFIOBRILMIZA QRUECURSOS PARA
D DESENVOLVIMENTO DE
APLICAÇÕES CORPORATIVAS
VOLTADAS PARA WEB E
SERVIDORES DE APLICAÇÃO.

« PROJETADA PARA SUPORTAR
SISTEMAS DE USO EM LARGA
ESCALA.

DESENVOLVIMENTO DE
APLICAÇÕES ESCALÁVEIS,
ROBUSTAS EMULTI CAMADAS.

* SEGURANÇA E CONFIABILIDADE.

JAVA ME

PLATAFORMA PARA
DESENVOLVIMENTO DE
APLICAÇÕES PARA
DISPOSITIVOS MÓVEIS E
SISTEMAS INTEGRADOS,

FORNECE UM
SUBCONJUNTO DA
FUNCIONALIDADE DO JAVA
SE

APRESENTA BIBLIOTECAS
ESPECÍFICAS PARA
DISPOSITIVOS MÓVEIS.

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

PASSAGEM DE PARÂMETROS POR VALOR

* CÓPIA DO VALOR 00 ARGUMENTO É PASSADA PARA 0 MÉTODO.

* APENAS SEU VALOR É PASSADO PARA A VARIÁVEL CORRESPONDENTE AO
PARÂMETRO

rPASSAGEM DE PARÂMETROS POR REFERÊNCIA

* 0 MÉTODO CHAMADO PODE ACESSAR 0 VALOR DO ARGUMENTO
NO CHAMADOR DIRETAMENTE E MODIFICAR ESSES DADOS, SE
NECESSÁRIO

* APRIMORA DESEMPENHO ELIMINANDO A NECESSIDADE DE
COPIAR QUANTIDADES DE DADOS POSSIVELMENTE GRANDES

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

MECANISMO QUE PERMITE QUE CARACTERÍSTICAS COMUNS
A DIVERSAS CLASSES SEJAM FATORADAS EM UMA CLASSE
BASE, OU SUPERCLASSE

CADA CLASSE DERIVADA OU SUBCLASSE APRESENTA AS
CARACTERÍSTICAS DA CLASSE BASE

JAVA OFERECE MECANISMOS PARA DEFINIR CLASSES DERIVADAS A PARTIR DE CLASSES EXISTENTES

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

MODIFICADORES | DESCRIÇÃD

A classe e/ou seus membros são acessíveis somente por classes do mesmo pacote,

DEFAULT OU PACKAGE

na sua declaração não é definido nenhum tipo de modificador, sendo este identificado pelo compilador. Permite que apenas classes do mesmo pacote tenham acesso as propriedades que possuem este modificador.
PUBLIC O código é acessível para todas as classes

Membros da classe definidos como private não podem ser acessados ou usados por nenhuma outra classe. Esse modificador não se aplica às classes, somente para seus
PRIVATE

métodos e atributos. Esses atributos e métodos também não podem ser visualizados pelas classes herdadas.
PROTECTED

O modificador protected torna o membro acessível às classes do mesmo pacote ou através de herança, seus membros herdados não são acessíveis a outras classes fora do pacote em que foram declarados.
Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Ju

* PHP é uma linguagem de programação de scripts, interpretada, de alto nível,
open-source,
gratuita, server-side, dinamicamente/fracamente tipada, estruturada e orientada a objetos,portável, robusta e eficiente utilizada para desenvolvimento web.

* Os Servidores Web mais populares são Apache (Software Livre) e IIS (Software
Proprietário). Uma vez instalado, configura-se o PHP, reinicia-se o servidor e está pronto para usar! OPHP fica embutido dentro do código HTML!
OPERADORES ARITMÉTICOS

SIGNIFICADO
IDENTIDADE
NEGAÇÃO
ADIÇÃO
SUBTRAÇÃO
MULTIPLICAÇÃO
DIVISÃO
MÓDULO
EXPONENCIAL

DESCRIÇÃO

Conversão de $a para int ou float
Oposto de $a.

Soma de $a e $b.
Diferença entre $a e $b.
Produto de saesb.

Quociente de $a e $b.

Resto de $a dividido por $b.

Resultado de $a elevado a $ò.

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo JürTO

ANOTAÇÃO SIGNIFICADO
DESCRIÇÃO

Verdadeiro (true) se sa é igual a sb.

Verdadeiro (true) se sa é igual a sb, e eles são do mesmo tipo.
Verdadeiro se sa não é igual a sb.

Verdadeiro se $a não é igual a $b.

Verdadeiro de $a não é igual a sb, ou eles não são do mesmo tipo
(introduzido no PHP4).

Verdadeiro se $a é estritamente menor que sb.
Verdadeiro se $a é estritamente maior que $b.
Verdadeiro se $a é menor ou igual a sb.

Verdadeiro se sa é maior ou igual a sb.

Um integer menor que, igual a ou maior que zero quando saé,

respectiva mente, menor que, igual a ou maior que sb.

OPERADORES INCREMENTAIS/DECREMENTAIS

ANOTAÇÃO | SIGNIFICADO

*+SA PRÉ-INCREMENTO
SA++ PÓS-INCREMENTO

~$A PRÉ-DECREMENTO
SA- PÓS-OECREMENTO

DESCRIÇÃO

Incrementa sa em um, e então retoma sa.
Retorna sa, e então incrementa sa em um.
Decrementa sa em um, e então retorna sa.
Retorna sa, e então decrementa sa em um.

OPERADORES LÓGICOS

ANOTAÇÃO | SIGNIFICADO
DESCRIÇÃO

Verdadeiro (true) se tanto sa quanto sb são verdadeiros.
Verdadeiro se sa ou sb são verdadeiros.

Verdadeiro se sa ou sb são verdadeiros, mas não ambos.
Verdadeiro se sa não é verdadeiro.

Verdadeiro se tanto sa quanto sb são verdadeiros.
Verdadeiro se sa ou sb são verdadeiros.

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

3. Tecnologias e práticas frontend web: HTML

Tecnologias e práticas frontend web: HTML

* HTML significa Hyper Text Markup Language.

* HTML é a linguagem de marcação padrão para criar páginas da Web;

* HTML descreve a estrutura de uma página da Web;

* HTML consiste em uma série de elementos;

* Os elementos HTML informam ao navegador como exibir o conteúdo;

* Os elementos HTML rotulam partes do conteúdo como "isto é um título", "isto é um parágrafo",
"isto é um link", etc.

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

LINGUAGEM DE MARCAÇÃO PADRÃO PARA CRIAR PÁGINAS DA WEB
DESCREVE A ESTRUTURA DE UMA PÁGINA DA WEB

CONSISTE EM UMA SÉRIE DE ELEMENTOS

ELEMENTOS HTML INFORMAM AO NAVEGADOR COMO EXIBIR 0 CONTEÚDO E ROTULAM PARTES
DO CONTEÚDO COMO "ISTO É UM TÍTULO", "ISTO É UM PARÁGRAFO", "ISTO É UM LINK", ETC.

HTML Básico cIDOCTYPE html>
<html>

<body>

Meu primeiro título.

<hl>Heu primeiro título.</hl>
Meu prtmetro parágrafo

<p>Meu primeiro parágrafo.</p>

</body>

</html>

Elementos HTML

Um elemento HTML é definido por uma tag inicial, algum conteúdo e uma tag final. O
elemento HTML
é tudo, desde a tag inicial até a tag final:

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Ju

< tagname > O conteúdo vai aqui... < /tagname >

< h1 > Meu primeiro cabeçalho < /h1 >

< p > Meu primeiro parágrafo. < /p >

Tag inicial conteúdo do elemento 1 Tag final

<h1> My First Heading </h1>

<P> My first paragraph. </p>

<br> none none cIDOCTYPE html>
<ht«l>

<body>

Meu primeiro título.

<hl>Meu primeiro título.</hl>
Meu primeiro parágrafo

<p>Meu primeiro parágrafo.</p>

</body>

</html>

Atributos HTML

Todos os elementos HTML podem ter atributos. Os atributos fornecem informações adicionais sobre os elementos, e são sempre especificados na tag de início. Os atributos geralmente vêm em pares de nome/valor como: name="value".
Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

Propriedade CSS Descrição

Background-color

Color
Font-family

Font-síze
Text-align

Define a cor de fundo de um elemento HTML
Define a cor do texto para um elemento HTML
Define a fonte a ser usada para um elemento HTML

Define o tamanho do texto para um elemento HTML

Define o alinhamento horizontal do texto para um elemento HTML

<B> TEXTO EM NEGRITO

<STRONG> TEXTO IMPORTANTE

<I>TEXTD EM ITÁLICO

<EM>

01182426

<MARK> TEXTO MARCADO

<SMALL> TEXTO MENOR

<DEL> TEXTO DELETADO

<INS> TEXTO INSERIDO

<SUB> TEXTO SUBSCRITO

<SUP> TEXTO SOBRESCRITO

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

Abreviação Formato do arquivo
Animated Portable Network Graphics
Graphics Interchange Format

Microsoft Icon

.apng

-gif

.ico, .cur

Extensão

Joint Photographic Expert Group image
Portable Network Graphics
Scalable Vector Graphics jpg, -jpeg, .jfif, .pjpeg, .pjp
,png

-svg

SRC DEFINE A URL DA IMAGEM

ALT DEFINE UM TEXTO ALTERNATIVO PARA UMA IMAGEM, SE ELA NÃO PUDER SER EXIBIDA

WIDTH E HEIGHT DEFINEM 0 TAMANHO DA IMAGEM

Tag Descrição

<ímg> Define uma imagem;

<map> Define um mapa de imagem;

<area> Define uma área clicável dentro de um mapa de imagem;

<picture> Define um contêiner para vários recursos de imagem.

Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Jui

<TABLE> DEFINE UMA TABELA

<TH> DEFINE UMA CÉLULA DE CABEÇALHO EM UMA TABELA

<TR> DEFINE UMA LINHA EM UMA TABELA

<TD> DEFINE UMA CÉLULA EM UMA TABELA

<CAPT1ÜN> DEFINE UMA LEGENDA DE TABELA

«COLGROUP> ESPECIFICA UM GRUPO DE UMA OU MAIS COLUNAS EM UMA TABELA PARA FORMATAÇÃO

<COL> ESPECIFICA AS PROPRIEDADES DA COLUNA PARA CADA COLUNA DENTRO DE UM ELEMENTO <COLGROUP>

<THEAD> AGRUPA 0 CONTEÚDO DO CABEÇALHO EM UMA TABELA

«TBODY» AGRUPA 0 CONTEÚDO DO CORPO EM UMA TABELA

<TFOOT> AGRUPA 0 CONTEÚDO DO RODAPÉ EM UMA TABELA

Um iframe (abreviação de "frame inline") é um elemento HTML usado para incorporar uma página daWeb em outra página da Web. Ele fornece uma maneira de exibir o conteúdo de outra página da Web na página da Web atual e é comumente usado para incorporar vídeos, mapas e outros conteúdos interativos.
Elizabeth Menezes de Pinho Alves, Leonardo Mathias, Paulo Ju

Vamos ficando por aqui.

Esperamos que tenha gostado do nosso Bizu!
Bons estudos!

