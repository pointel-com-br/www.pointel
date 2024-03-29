# Garantia da Segurança de Sistemas - Controle de acesso. Assinatura e Certificação digital

Índice

1) Assinatura Digital

2) Certificação Digital

3) ICP - Infraestrutura de Chaves Públicas - PKI (Public Key Infrastructure)

4) Aplicações de Criptografia

ASSINATURA DIGITAL

A assinatura digital é um recurso extremamente importante e muito presente nas diversas aplicações atualmente. Seu princípio básico reside na obtenção dos princípios de integridade e autenticidade na troca de mensagens entre dois usuários.
Para tanto, vamos analisar a figura a seguir:

Como já vimos, o tipo de criptografia utilizada é a assimétrica. Isso quer dizer que teremos um par de chaves (pública e privada), envolvidas no processo.
Percebemos que temos dois fluxos a serem analisados que fazem parte de um mesmo processo de assinatura digital. Na figura acima, na esquerda, temos o fluxo responsável por garantir a autenticidade. Na direita, temos o fluxo que garante a integridade.
Analisando o fluxo da esquerda, temos algo semelhante ao processo de autenticidade que vimos na criptografia assimétrica. Entretanto, antes de se aplicar o algoritmo de chaves públicas, realiza-se a função HASH no texto em claro. Portanto, sequencialmente, temos:
1. Gera-se o HASH da mensagem em claro;

2. Aplica-se o algoritmo de criptografia assimétrica utilizando a chave privada do
EMISSOR sobre o HASH gerado no passo 1;

3. Tem-se a Assinatura Digital;

4. Envia-se ao destinatário a Assinatura Digital gerada e a mensagem original;

/ 25

/

No lado do destinatário, este deverá primeiramente utilizar a chave pública do EMISSOR.
Ao realizar tal procedimento, obtém-se o HASH da mensagem original. Como o destinatário também recebeu de forma direta o HASH, ele poderá comparar o conteúdo das duas mensagens.
Caso sejam iguais, podemos dizer que o emissor é de fato o dono da chave pública utilizada(autenticidade) e que não houve alteração na mensagem (integridade).

Percebam que o foco nesse cenário não é garantir a confidencialidade, mas tão somente os outros dois princípios, até porque, a mensagem vai em aberto.
Existe ainda o conceito de temporalidade na Assinatura Digital.

Na assinatura atemporal, realiza-se o processo visto anteriormente sem nenhum registro de timestamp, ou seja, de data e hora dos procedimentos realizados.
Já a assinatura temporal envolve o registro de data e hora de quando foi realizada a assinatura.

Complementando o assunto sobre Assinatura Digital, algumas questões aparecem cobrando um arranjo diferente, o qual chamamos de Assinatura Digital Simétrica.
Vimos anteriormente o modelo utilizando algoritmos de criptografia assimétrica. Já o modelo que apresento a seguir independente das chaves privadas e públicas, mas tão somente da chave simétrica.
Entretanto, temos um pressuposto nesse modelo, que é o conhecimento mútuo da chave secreta.

Desse modo, o EMISSOR gera um HASH de uma mensagem concatenada com a chave secreta e envia juntamente com a própria mensagem em claro. O DESTINATÁRIO, ao receber este conjunto,pegará a mensagem em claro recebida, concatenará com a chave secreta que já é de seu conhecimento e também gerará um HASH.
Em seguida, basta ele comparar o HASH gerado com o HASH recebido. Caso sejam idênticos, assume-
se que a mensagem é autêntica e íntegra.

CERTIFICAçÃo DIGITAL

Vimos nas sessões anteriores a importância de uma série de alternativas para o uso do par de chaves na criptografia assimétrica. Entretanto, uma pergunta ficou no ar. Como confiar em uma chave pública? Ou seja, a chave pública de determinado usuário é realmente dele?
Inevitavelmente devemos envolver uma terceira parte para tal. Surge então o conceito deAutoridade Certificadora - AC (CA - Certification Authority).

Desse modo, pode-se inserir as informações de chave pública e muitas outras em um certificado digital. Entretanto, para que um certificado seja válido, deve ter sido emitido por uma CA. As CA's são entidades confiáveis que emitem e atestam certificados. Algo semelhante ao papel de um cartório, que validam as assinaturas dos cidadãos.
Para que a CA também seja uma parte confiável, a sua chave pública deve ser amplamente difundida de tal modo que todos possam conhecer e atestar a sua assinatura digital nos certificados gerados,dificultando bastante possíveis fraudes.

As principais informações contidas em um certificado digital são:

* Chave pública do usuário ou sistemas;

* Dados relativos à sua identidade;

* Prazo de validade;

* Assinatura Digital da Entidade Certificadora que gerou o certificado;

* Chave pública da CA

* Cadeia de certificados hierarquicamente superiores;

Além disso, por seguir o padrão X.509 do ITU-t, consta ainda:

* Versão do X.509 e número de série do certificado;

* Informação do algoritmo gerador do certificado;

* Identificação do gerador do certificado;

* Informações sobre o algoritmo assimétrico da chave pública do usuário;

A utilização de certificados digitais permite agregar os princípios de autenticidade e integridade por intermédio da utilização da assinatura digital e como diferencial, possui a capacidade de garantir ainda a confidencialidade. Para tanto, diversas alternativas podem ser utilizadas como a utilização da chave pública do destinatário ou ainda a utilização de chaves de sessão por meio de chaves simétricas.
Desse modo, vamos analisar a figura a seguir para entendermos bem o seu funcionamento:

Hash calculado por B

Hash calculado por A

Assinatura digital de A
pública de A

Assinatura digital de A
Podemos perceber na figura a garantia dos três princípios: confidencialidade,
integridade e autenticidade. No modelo em análise, será utilizada uma chave de sessão através da troca de uma chave simétrica.
Para começar, "A" cifra a mensagem com a chave simétrica gerada. Até então,
"B" não tem conhecimento dessa chave. Para que "B" tenha conhecimento, "A" cifrará a chave simétrica utilizando a chave pública de "B". Com isso, somente "B" será capaz de obter a chave simétrica através de sua chave privada, certo? Assim, a partir de então, "B" terá conhecimento da chave simétrica e poderá utilizá-la para decriptar a mensagem.
Entretanto, "B" precisa garantir que "A" é de fato quem diz ser. Para tanto,
utiliza-se o princípio da assinatura digital que vimos anteriormente. "A" calculará o HASH da mensagem e cifrará com a chave privada de "A". Portanto, a única chave capaz de abrir essa mensagem será a chave pública de "A". Assim, "B" utilizará a chave pública de "A" e obterá o HASH calculado por"A". Antes de realizar a comparação, "A" deverá pegar a mensagem original recebida e decriptada pela chave simétrica e calcular o HASH.
Q-Q SERPRO (Analista - Especialização: Tecnologia) Segurança da Informação -
2023 (Pós-Edital) 6

Caso ambas sejam iguais, tem-se a garantia dos três princípios.

Mais uma vez pessoal, é muito importante que entendam o modelo para ficar claro o funcionamento. As diversas tecnologias que utilizam certificados digitais usam esse modelo como base. Acrescentam-se alguns passos, elementos de validação, como a AutoridadeCertificadora,
entre outros, porém, o princípio é o mesmo.

ICP - INFRAESTRUTURA DE CHAVES PÚBLICAS - PKI
(PUBLIC KEY INFRASTRUCTURE)

Todo o conjunto de hardware e software, pessoal, políticas e procedimentos necessários para criar e implementar uma infraestrutura de certificação digital chama-se PKI ou ICP.É uma estrutura hierárquica que permite uma melhor organização e gerenciamento dos certificados, além de tratar aspectos de auditabilidade e controle.
Esta pode ser composta por quatro componentes básicos:

Autoridade Certificadora - (CA - Certificate Authority)
Autoridade Registradora - (RA - Registration Authority)
Certificados Digitais

Lista de Certificados Revogados (CRL- Certification Revocation List)

Vamos falar um pouquinho sobre cada um deles.

AUToRIDADE CERTIFICADoRA - AC

Como vimos, é a responsável pela emissão dos certificados digitais. Antes de iniciar o processo de emissão, a AC deverá processar as requisições de emissão por parte dos clientes com os devidos parâmetros apresentados.
As requisições de certificado também devem seguir uma rotina e padrão para que seja válida e aceita. A estrutura dessa requisição deve contemplar, basicamente:
1. Informação de Requisição do Certificado;

2. Identificador do Algoritmo de Assinatura;

3. Assinatura Digital da Informação de Requisição;

Além disso, a AC é responsável pela manutenção e gerenciamento da lista de
Certificados
Revogados, devendo publicar essa informação

SERPRO (Analista - Especialização: Tecnologia) Segurança da Informação - 2023
(Pós-Edital)

Outra função presente na AC é responder às requisições de consultas de verificação de certificados geradas pelos clientes com vistas a validação dos certificados.
Autoridade Certificadora Raiz - AC Raiz

Como a PKI possui uma estrutura hierarquizada, a AC Raiz surge para ser a entidade mais alta dentre as diversas AC's que podem compor uma PKI. Assim, pode-se ter uma estrutura rígida, confiável e descentralizada em termos de papéis e operação.
A AC Raiz se utiliza do recurso de certificado auto-assinado. Como ela é o primeiro elemento de uma infraestrutura, não há nenhum outro elemento que possa validar sua assinatura. Por esse motivo, ela deve ser de conhecimento amplo e difundido.Uma prática de segurança é, após a geração desse certificado, deixar a AC Rais off-
line, religando-a apenas para emissão de um novo certiticado auto-assinado.

Um outro conceito importante é que para um certificado ser válido, toda a cadeia de
CA's deve possuir certificados válidos. Ou seja, como a PKI é uma estrutura multinível,
todos os níveis ascendentes devem ser validos.

Uma outra questão a ser discutida é a relação de confiança entre AC's Raiz. Desse modo, essas AC's trocam informações entre si e os certificados de uma passam a ser aceitos e válidos para toda a cadeia da outra AC Raiz. Esse modelo é amplamente utilizado na comunicação de AC's Raiz de países distintos ou de empresas distintas.Esse tipo de relacionamento é conhecido como Bridge.

Caso haja mais de duas AC's Raiz que possuem relação de confiança mútua,
chamamos de modelo Misto.

AUToRIDADE REGISTRADoRA - AR

Algumas estruturas de PKI permitem segmentar os papéis e funcionalidade presentes na
AC, a saber:
registro, emissão e validação.

Assim, a principal função de uma AR é funcionar como um intermediário na comunicação entre cliente e AC, reduzindo a sobrecarga na AC. Importante deixar claro que a AR não possui permissão e capacidade de EMITIR CERTIFICADOS.
Entretanto, pode exercer as seguintes funções:

1. Distribuir chaves;

2. Receber e aceitar registros;

3. Validar requisições de verificação de certificado;

A Autoridade de Registro pode estar localizada fisicamente em conjunto com a AC ou localizada remotamente em outros servidores. Além disso, ela não é obrigatória na estrutura da PKI.
CERTIFICADoS DIGITAIS

A seguir, temos um breve exemplo de algumas informações que estão presentes em um certificado digital.
SERPRO (Analista - Especialização: Tecnologia) Segurança da Informação - 2023
(Pós-Edital)

Para os alunos que estão estudando em frente a um computador, recomendo darem uma olhada nos certificados digitais de algum site que tenham costume de navegar. Por exemplo,basta clicar no cadeado fechado e buscar a opção de verificar o certificado digital.
No exemplo em questão, podemos verificar algumas informações. O referido certificado digital foi emitido para o domínio www4.receita.fazenda.gov.br.
A Autoridade Certificadora responsável por emitir tal certificado é a "Autoridade
Certificadora do
SERPRO SRF vl". Ora pessoal, aqui já começamos a identificar uma estrutura hierárquica de uma infraestrutura de chaves públicas.
Além disso, avançando para a aba de "caminho de certificação", utilizando o navegador
CHROME,
obtemos a imagem abaixo:

Certificado

Geral Detalhes Caminho de Certificação
Caminho de certificação

Ejjl Autoridade Certificadora Raiz Brasileira v2

L-Eftl AC Secretaria da Receita Federal do Brasil v3

Auto ri d a d e Ce rtifi ca d o ra S ERPRO RFBv4
www4. receita .fazen d a. g ov. br

Exibir Certificado

Status do certificado:

Este certificado é válido.

Na imagem a seguir, vemos qual foi a Autoridade Certificadora raiz que valida todas as demaisAutoridades Certificadoras abaixo dela, dando validade também ao certificado.

Os browsers atuais já possuem instalados diversas autoridades certificadoras reconhecidas mundialmente. Assim, qualquer certificado que faça parte de uma dessas estruturas, será considerado como válido de forma nativa.
Tais certificados geralmente são pagos e mantidos por terceiros.

Entretanto, temos um modelo em que queremos gerar certificados digitais internos a uma organização ou para troca entre duas ou mais organizações que confiam entre si mutuamente.
Entretanto, ao acessarmos esses serviços com certificados digitais e que não façam parte da estrutura de certificados emitidos por Autoridades Certificadoras nativamente reconhecidas pelosBrowsers, receberemos um alerta, como algo do tipo da imagem abaixo:

Sua conexão não é particular

Invasores podem estar tentando roubar suas informações de webmail.sdh.gov.br (por exemplo, senhas, mensagens ou cartões de crédito). NET::ERR_CERT_AUTHoRITY_INvAUD
Avançado
Voltar à segurança

Nesse caso, para que o Browser pare de gerar os alertar em questão, basta instalar a cadeia de certificados, ou seja, a cadeia das Autoridades Certificadoras que emitiram o referido certificado.Assim, o Browser, a partir desse momento, considerará como válido quaisquer certificados emitidos por este novo grupo de CA's.
Este conceito é denominado como certificados auto assinados, pois não há uma terceira parte confiável que dê a devida veracidade a essas informações.
LISTA DE CERTIFICADoS REVoGADoS - CRL

Os certificados digitais devem possuir plena validade para serem devidamente reconhecidos e utilizados pelos diversos sistemas e serviços. Entretanto, algumas questões podem surgir no dia a dia de utilização que implicam em tornar esses certificados inválido e,portanto, devem ser revogados.
Para que isto ocorra, podemos citar alguns exemplos:

1. Caso o prazo de validade do certificado expire;

2. Caso o usuário perca a informação de sua chave privada e não haja custódia de um terceiro;

3. Caso haja violação da chave privada, ou seja, algum terceiro obtenha a informação da chave privada de um usuário ou sistema.
Todos esses certificados inválidos figuram então na lista de certificados revogados e ficam disponíveis para consulta por parte dos clientes.
OCSP - Online Certificate Status Protocol

Este protocolo foi criado para resolver problemas de troca de listas de certificados revogados. A principal dificuldade é que o cliente ou servidor que deseja verificar essa lista deve realizar download desta constantemente com vistas a manter sua base atualizada.
Com o uso do OCSP, não há necessidade de download da lista. O procedimento agora é bem mais simplificado, pois basta ser enviado o número de série do certificado para o servidor OCSP e este será responsável por verificar em uma lista atualizada,respondendo a consulta com o status obtido.

ICP BRASIL

No Brasil, temos uma PKI a nível nacional, conhecida como ICP Brasil, controlada pelo governo brasileiro que agrega legitimidade aos certificados digitais no nosso país.Desse modo, esses certificados possuem validade com plena eficácia, sendo capazes de produzir efeitos jurídicos.Entretanto, é importante mencionar que há pessoas jurídicas de direito privado como AC's e AR's.

As principais informações a respeito da ICP Brasil podem ser obtidas no site www.iti.gov.br/icp-brasil.Desse modo, podemos extrair a definição do ICP-Brasil do próprio site:

"A Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil) é uma cadeia hierárquica e de confiança que viabiliza a emissão de certificados digitais para identificação virtual do cidadão.Observa-se que o modelo adotado pelo Brasil foi o de certificação com raiz única,
sendo que o ITI,

além de desempenhar o papel de Autoridade Certificadora Raiz (AC-Raiz), também tem o papel de credenciar e descredenciar os demais participantes da cadeia, supervisionar e fazer auditoria dos processos"
O responsável pela definição das diretrizes e políticas a serem aplicadas à ICP Brasil é o ComitêGestor da ICP Brasil. Assim, compete à AC Raiz dessa ICP emitir, expedir, distribuir,
revogar e gerenciar os certificados das autoridades certificadoras de nível imediatamente inferior ao seu.Possui ainda como competência a fiscalização e responsabilidade de auditoria das AC's,
AR's e demais prestadores de serviço.
A hierarquia completa de todas as AC's e AR's que compõem a ICP Brasil pode ser obtida no link:http://www.iti.gov.br/images/icp-

brasil/estrutura/2015/011 novembro/atualizacao 28/estrutura completa.pdf

Um ponto que recorrentemente cai em prova são as definições constantes no Glossário da
ICP Brasil que consta no link:http://www.iti.gov.br/images/twiki/URL/pub/Certificacao/Glossario/Glossario ICP Brasil Versão
1.2 nov o-2.pdf
Sugiro uma leitura desse documento pelo menos uma vez para se ter uma visão geral das definições.

A seguir, apresento ainda um tópico que tem caído em algumas provas.

* Tipos de Certificados Digitais:

o Certificado de Assinatura Digital (Al, A2, A3 e A4)

São os certificados usados para confirmação da identidade na web, correio eletrônico, transações online, redes privadas virtuais, transações eletrônicas,informações eletrônicas, cifração de chaves de sessão e assinatura de documentos com verificação da integridade de suas informações.
o Certificado de Sigilo (Sl, S2, S3 e S4)

São os certificados usados para cifração de documentos, bases de dados,
mensagens e outras informações eletrônicas.

o Certificado do Tipo Al e Sl

É o certificado em que a geração das chaves criptográficas é feita por software e seu armazenamento pode ser feito em hardware ou repositório protegido por senha, cifrado por software. Sua validade máxima é de um ano, sendo a frequência de publicação da LCR no máximo de 48 horas e o prazo máximo admitido para conclusão do processo de revogação de 72 horas.
o Certificado do Tipo A2 e S2

É o certificado em que a geração das chaves criptográficas é feita em software e as mesmas são armazenadas em Cartão Inteligente ou Token, ambos sem capacidade de geração de chave e protegidos por senha. As chaves criptográficas têm no mínimo 1024 bits. A validade máxima do certificado é de dois anos, sendo a frequência de publicação da LCR no máximo de 36 horas e o prazo máximo admitido para conclusão do processo de revogação de 54 horas.
o Certificado do Tipo A3 e S3

É o certificado em que a geração e o armazenamento das chaves criptográficas são feitos em cartão Inteligente ou Token, ambos com capacidade de geração de chaves e protegidos por senha, ou hardware criptográfico aprovado pela ICP-Brasil. As chaves criptográficas têm no mínimo 1024 bits. A validade máxima do certificado é de três anos, sendo a frequência de publicação da LCR no máximo de 24 horas e o prazo máximo admitido para conclusão do processo de revogação de 36 horas.
o Certificado do Tipo A4 e S4

É o certificado em que a geração e o armazenamento das chaves criptográficas são feitos em cartão Inteligente ou Token, ambos com capacidade de geração de chaves e protegidos por senha, ou hardware criptográfico aprovado pela ICP-Brasil. As chaves criptográficas têm no mínimo 2048 bits. A validade máxima do certificado é de três anos, sendo a frequência de publicação da LCR no máximo de 12 horas e o prazo máximo admitido para conclusão do processo de revogação de 18 horas.
Ainda no âmbito da ICP Brasil, podemos categorizar os certificados considerando o usuário ou sistema que irá utilizá-lo. Nesse sentido, podemos fazer a primeira distinção, quais sejam:
* Pessoa Física (e-CPF;

* Pessoa Jurídica (e-CNPJ);

* Sistemas;

Então a depender da utilização, devemos trabalhar com tipos diferenciados de certificados. Vamos fazer algumas considerações de cunho prático sobre os certificados, tendo em vista que é um assunto novo em provas, porém, já tem aparecido nos editais. Apenas destacar que noBrasil, como já mencionamos, os certificados possuem validade jurídica e fiscal... Então é possível realizar atos legais a partir do certificado digital.
1. e-CPF

a. Utilizado para pessoa física;

b. Tem a mesma validade jurídica que um CPF;

c. Não ser para emissão de Nota Fiscal Eletrônica;

d. Alguns serviços que suportam sua utilização:

i. Declaração de Imposto de Renda;

ii. Serviços Gerais da Receita Federal, entre outros serviços da justiça, saúde e educação;
2. e-CNPJ

a. Utilizado por pessoa jurídica;

b. Versão digital do CNPJ da empresa;

c. Amplamente utilizado para simplificação e desmaterialização de processos,
permitindo otimizar o tempo e reduzindo custos legais e operacionais;

d. Alguns serviços que suportam sua utilização:

i. Entregar Declaração de imposto de Renda e outras declarações de empresa;

ii. Serviços diversos da Receita Federal;

iii. Serviços Gerais da Receita Federal, entre outros serviços da justiça, saúde e educação;
iv. Outros serviços como o sistema social da CAIXA (FGTS), sistema integrado de comércio exterior (Siscomex);
EV SSL (Validação Avançada)

Como já mencionamos, os Certificados Digitais são ancorados nas tecnologias
SSL/TLS. Considerando a navegação web dos usuários, um consórcio de especialistas na Internet criou uma metodologia, a partir de 2007, que permite a identificação por parte dos Browsers de que os sites utilizam o certificado digital.
São os famosos cadeados verdes, o URL's verdes que aparecem nos browsers.
Com isso, é muito mais fácil combater o PHISHING (falsificação de páginas),
chamando a atenção do usuário de maneira simples a partir do browser sobre a confiabilidade deste.
Cada Browser apresenta o resultado de uma forma. No Caso do Google
Chrome, podemos ver o símbolo conforme acima. Destaca-se que o processo de obtenção do certificado passa por uma sequência de ações e comprovação de documentos para gerar a maior confiabilidade possível.
Considerando a utilização de certificados digitais nas páginas web, temos que a vinculação do certificado, em regra, se dá para determinada URL. Nesse sentido, por exemplo, cria-se um certificado digital que será utilizado pelo site do ESTRATÉGIA CONCURSOS, por exemplo,que seria para a URL- .
Desse modo, todas as chamadas feitas para dentro do domínio em questão, são aceitas,
como por exemplo:
https://www.estrategiaconcursos.com. br/cursosPorProfessor/andre-castro-3353/

SERPRO (Analista - Especialização: Tecnologia) Segurança da Informação - 2023
(Pós-Edital)

Percebam que se trata de uma mesma URL, havendo distinção apenas dos objetos que são chamados a partir do site, ou seja, diretórios do servidor web.
Agora imagine que se deseja criar subdomínios distintos a partir de uma mesma URL
padrão. Vamos supor que o objetivo seja criar três subdomínios para o ESTRATÉGIA conforme abaixo:
* www.alunos.estrategiaconcursos.com.br

* www.professores.estrategiaconcursos.com.br

* www.administrativo.estrategiaconcursos.com.br

Considerando o certificado padrão, seriam necessários 3 certificados digitais, sendo um para cadaURL... Percebam que a URL mudou, ainda que sejam vinculados a uma mesma raiz.

Nesse contexto surgem os certificados digitais WILDCARDS. Com esse certificado, pode-se utilizar ilimitados subdomínios. Diz-se, portanto, que se deve emitir o certificado para o domínio www.*.estrategiaconcursos.com.br.
Ou seja, o símbolo representa as possíveis variações dos subdomínios.

Mas você, aluno fiel do professor André Castro, está sempre pensando à frente. E
sabendo do crescimento da maior empresa de concursos do país, iria fazer a seguinte pergunta:
"André, mas na taxa de crescimento do estratégia, como impedir que outros sites tentem utilizar o mesmo nome com outras extensões? E se o ESTRATÉGIA quisesse ter visibilidade para o mundo com o domínio .com?"
Bom, aí surgem os certificados conhecidos como SAN (Subject Alternate Name).
Podem ser referenciados também como UCC (Unified Communication Certificate). Na prática, são conhecidos como certificados "Multi-Domínio".
Nesse sentido, a ideia é gerar um único certificado que suporte outros domínios, por exemplo:

*

* www estrategiaconcursos.com

* www.administrativo.estrategiaconcursos.net

* Entre outros

A figura abaixo nos dá um exemplo do site da geotrust, considerando esse contexto:

Safari is using an encrypted connectron to www.geotrusLcom.

Encryption with a digital certificate keeps information private as it's sent to or from the https website www.geotrust.com.
CeoTrust Inc has identified www.geotrust.com as being owned by CeoTrust,
Inc. in Mountain View. Califórnia, US.

CeoTrust Primary Certification Authority
CeoTrust Extended Vaiidation SSL CA

u www. ge otru st.co m

Extension Extended Key Usage ( 2.5.29.37 )

Criticai NO

Purpose #1

Purpose #2

Server Authentication ( 1.3.6.1.5.5.7.3.1)
Client Authentication ( 1.3.6.1.5.5.7.3.2 )

Extension Authority Key Identifier ( 2.5.29.35 )

Criticai NO

Key ID 28 C4 EB 8F F1 5F 79 90 A3 28 55 C3 56 4E 70 6B 53 72 2C

Extension 5ubject Alternative Name ( 2.5.29.17)

Criticai NO

DN5 Name www.geotrust.net
DN5 Name www.geot ru st. com
DN5 Name geotrust.com

Extension
Criticai
Policy ID #1

Qualifier ID #1

CPS URI

Certificate Policies ( 2.5.29.32 )
NO

( 1.3.6.1.4.1.14370.1.6)

Certificalion Practice Statement( 1.3.6.1.5.5.7.2.1 )
htt D : / www.g eot ru s t. co mre so u ice s c ps

Extension
Criticai

CRL Distribiution Points ( 2.5.29.31 )
NO

URI http: / / EV5 5 L - c rl. qe otru st. c o m /cr 1 s / q textval c a.crl

Extension
Criticai
Method #1

Certificate Authority Information Access ( 1.3.6.1.5.5.7.1.1 )
NO

Online Certificate Status Protocol ( 1.3.6.1.5.5.7.48.1 )

URI http: / / EV5 5 L - ocs p. q eotru st. com

Hide Certificate 0K

APLICAçõES DE CRIPToGRAFIA

Algumas bancas têm cobrado alguns assuntos mais específicos no que tange a conceitos atrelados a aplicações que dependem da criptografia como base de seu funcionamento. Entretanto,apesar de constar nos editais, não tenho visto esses assuntos caírem nas provas e, por isso, a ausência de questões sobre o assunto.
CRIPToMoEDAS E BLoCKCHAIN

Tudo se ancora no conceito de moeda digital. No modelo antigo, tínhamos entes centrais que atuavam como garantidores dos recursos e fundos. Ou seja, um banco, por exemplo, era capaz de dizer para a parte tomadora do recurso se, de fato, você tem aquele crédito ou não para realizar a operação. Muito básico para a realidade que temos hoje, certo?
Entretanto, o surgimento das criptomoedas vão além desse cenário restrito. O pseudônimo
SATOSHI
NAKAMOTO foi o responsável por essa façanha.

Ele publicou um artigo conhecido como "Bicoint: A Peer-to-Peer Electronic Cash System".

Em seu artigo, ele cria um modelo de moeda digital descentralizado, sob o conceito de criptomoeda e comunicação peer-to-peer. Além disso, aplica metodologias de pagamento eletrônico baseado em garantias criptográficas e não na relação de confiança, como existia antes com os bancos. Ou seja,não há gerencimaneot por instituições financeiras.

O BITCOIN está amparado em 4 pilares básicos, quais sejam:

1. Transações

2. Garantia do trabalho;

3. Mineração;

4. Carteira Digital;

Dessa forma, ao mesmo tempo que o modelo prevê um acesso e utilização de forma pública, há um caráter de zelar pela anonimidade em todo o processo, o que, infelizmente, é utilizado por muitos como forma de gerar fluxos financeiros de maneira ilícita e, portanto, não rastreável.
*

Em relação ao seu funcionamento, tem-se a criação de blocos transacionais, onde cada bloco possui informação das transações atuais, bem como links para os blocos anteriores, inclusive com relação até o primeiro bloco. Daí surge o conceito de BLOCKCHAIN. Em cada bloco, tem-se o valor de referência de 25 bitcoins por bloco.
Uma das diferenças que agrega confiabilidade ao processo é o fato de se ter o armazenamento do"arquivo block chain" em cada nó envolvido na rede do blockchain, e não de maneira centralizada em um nó ou datacenter de um grande branco. Assim, é possível que os nós envolvidos na transação tenham condições de conferir se tais arquivos não foram adulterados de maneira simples e fácil. Ou seja, se alguém tem a intenção de adulterar tal conteúdo, deverá também alterá-lo em todos os nós da rede, o que é, na prática, impossível.
Aqui vale a máximo de que, a minoria de usuários que tentam burlar o processo não terá força para"alterar" alguma informação sem a anuência e confirmação da "maioria honesta".
Importante destacar que essa operação será considerada válida somente após ser validada por 6 nós aleatórios.Tão logo seja validada, ela é propagada para toda a rede para registro nos arquivos da blockchain e armazenamento do histórico.
Nesse contexto, surgem os mineradores. São responsáveis por gerarem os blocos e processarem os algoritmos de cada transação. Quanto mais mineradores na rede, mais robusto se torna o sistema.
Esses mineradores são remunerados por intermédio de comissões do sistema,
intrínsecos ao modelo. Justamente por demandar grande poder de processamento, utiliza-se de placas gráficas em paralelo para tal finalidade. Não é muito difícil se encontrar placas de videogames sendo utilizadas para tal propósito.
Essas comissões são geradas em um regime descrescente. Ou seja, a cada 10 minutos,
gera-se uma quantidade de bitcoins para ser distribuída entre os mineradores. O regime decrescente apresenta um cenário em que a quantidade de bitcoins geradas a cada 10 minutos então vai reduzindo, até que chegue ao limite do modelo, que é de 21 milhões de bitcoins. Nesse momento, não serão geradas mais comissões.
Uma forma de controlar a geração dos bitcoins a cada 10 minutos se dá pelo fato de aumentar, cada vez mais, a complexidade dos cálculos matemáticos. Ou seja, ainda que se aumente o poder computacional, os processos vão ficando cada vez mais difíceis, traçando um comportamento em termos de período mais uniformes.
Todas as transações e blocos ficam armazenadas em um "livro de registro". Essas transações são conhecidas por terem como característica o fato de "serem de difícil solução (por isso exigem muito processamento), porém, de fácil comprovação". Obviamente não discutiremos o funcionamento do algoritmo.
A título e registro, temos a utilização da função HASH SHA256.

Todo o processo de criptografia e identificação das entidades envolvidas são ancoradas no processo de assinatura digital (chaves públicas e privadas).
Falando um pouco mais da blockchain, é importante destacar que a utilização dos pares de chaves pelos usuários se dá pelos seguintes motivos:
1. Chave pública é de amplo acesso e permite que qualquer usuário saiba da existência de uma conta ou carteira digital para usuários específicos.
2. Entretanto, a chave privada, de conhecimento exclusivamente do dono é que permite o acesso aos dados e informações, bem como autoriza e realiza transações para a referida carteira. Nada mais do que a aplicação dos conceitos da criptografia assimétrica.
Importante destacar que os conceitos atrelados à blockchain não se restringem a redes para troca de criptomoedas. Atualmente, diversas soluções podem utilizar a blockchain como um protocolo de confiança digital para uma infinidade de aplicações, como emissão de diplomas,certificados,
operações governamentais, decisões coletivas, apostas, seguros, certidões, entre muitos outros.

Então basicamente, tem-se uma rede para registrar e garantir os documentos envolvidos.

Nessa mesma linha de raciocínio é que surge o conceito de ALTCOINS. Simplesmente são outras criptomoedas ou soluções baseadas em blockchain com seus modelos próprios e aplicações específicas. Com pesquisas simples na Internet é possível identificar uma infinidade deALTCOINS já disponíveis no mercado.
