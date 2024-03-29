# Mecanismos de segurança - Criptografia simétrica

A criptografia simétrica, também conhecida como criptografia de chave secreta, é um método de criptografia em que uma única chave é usada tanto para criptografar quanto para descriptografar os dados. Isso significa que a mesma chave é compartilhada entre o remetente e o destinatário da mensagem.
No processo de criptografia simétrica, o remetente converte os dados legíveis (conhecidos como texto claro ou plaintext) em uma forma ilegível (conhecida como texto cifrado ou ciphertext) usando a chave secreta. O destinatário, por sua vez, usa a mesma chave para reverter o processo, ou seja, descriptografar o texto cifrado e obter novamente o texto claro original.
A criptografia simétrica é mais rápida e eficiente do que a criptografia assimétrica, pois requer menos recursos computacionais. Além disso, é amplamente utilizada para proteger dados confidenciais, como comunicações em redes locais, armazenamento local de dados sensíveis e criptografia de arquivos.
No entanto, há um desafio importante na criptografia simétrica, que é o compartilhamento seguro da chave. Uma vez que a mesma chave é usada para criptografar e descriptografar, é crucial que a chave seja mantida em segredo absoluto e seja compartilhada apenas entre as partes autorizadas. Se a chave for comprometida, um atacante pode acessar e descriptografar os dados protegidos.

Alguns algoritmos de criptografia simétrica comumente usados incluem:

1. AES (Advanced Encryption Standard): É um algoritmo amplamente adotado que suporta tamanhos de chave de 128, 192 e 256 bits.

2. DES (Data Encryption Standard): É um algoritmo mais antigo que usa uma chave de 56 bits. Embora ainda seja usado em algumas aplicações, é considerado menos seguro em comparação com o AES.

3. 3DES (Triple Data Encryption Standard): É uma versão mais segura do DES, que aplica o algoritmo DES três vezes usando duas ou três chaves diferentes.

4. Blowfish: É um algoritmo simétrico rápido e flexível, que suporta tamanhos de chave variáveis.

É importante ressaltar que, embora a criptografia simétrica seja eficaz para proteger a confidencialidade dos dados, ela não fornece autenticação ou garantia de integridade dos dados. Portanto, é comum combinar a criptografia simétrica com outros mecanismos de segurança, como assinaturas digitais ou criptografia assimétrica, para obter um sistema mais completo e seguro.

## Como funciona o algoritmo de criptografia ECB

O algoritmo de criptografia ECB (Electronic Codebook) é um modo de operação utilizado em algoritmos de criptografia de bloco, como o AES (Advanced Encryption Standard). O ECB é um modo de operação simples, onde cada bloco de dados é criptografado independentemente, sem levar em consideração os blocos anteriores ou o contexto.

Aqui está uma explicação de como o algoritmo de criptografia ECB funciona:

1. Divisão em blocos: O texto original a ser criptografado é dividido em blocos de tamanho fixo, geralmente 64 bits ou 128 bits.

2. Criptografia dos blocos: Cada bloco de dados é criptografado separadamente usando o algoritmo de criptografia de bloco, como o AES. O bloco criptografado resultante substitui o bloco de dados original.

3. Descriptografia dos blocos: Para descriptografar, cada bloco de dados criptografado é descriptografado separadamente usando o algoritmo de descriptografia de bloco. O bloco descriptografado substitui o bloco criptografado.

O processo de criptografia e descriptografia é realizado bloco por bloco, sem considerar o contexto dos blocos anteriores. Isso significa que, se houver padrões repetitivos ou blocos idênticos no texto original, eles serão criptografados para o mesmo bloco criptografado, o que pode resultar em uma perda de segurança. Além disso, o modo ECB não fornece confidencialidade para além dos próprios blocos de dados, o que significa que informações adicionais, como padrões ou estrutura, podem ser inferidas a partir dos blocos criptografados.

Devido a essas limitações de segurança e confidencialidade, o modo ECB não é recomendado para o uso geral em criptografia. Modos de operação mais seguros, como CBC (Cipher Block Chaining) ou CTR (Counter Mode), são preferíveis para garantir uma criptografia mais robusta e confiável, especialmente quando se trata de proteger dados sensíveis.

## Como funciona o algoritmo de criptografia CBC

O algoritmo de criptografia CBC (Cipher Block Chaining) é um modo de operação utilizado em algoritmos de criptografia de bloco, como o AES (Advanced Encryption Standard), para garantir a confidencialidade e integridade dos dados. O CBC é um modo de operação que adiciona um elemento de feedback ao processo de criptografia, tornando cada bloco de dados dependente dos blocos anteriores.

Aqui está uma explicação de como o algoritmo de criptografia CBC funciona:

1. Divisão em blocos: O texto original a ser criptografado é dividido em blocos de tamanho fixo, geralmente 64 bits ou 128 bits.

2. Vetor de inicialização (IV): Um vetor de inicialização aleatório é gerado e utilizado como entrada para o primeiro bloco de dados.

3. Operação XOR: O primeiro bloco de dados é combinado com o vetor de inicialização usando a operação XOR (OU exclusivo). O resultado é criptografado usando o algoritmo de criptografia de bloco, como o AES, produzindo um bloco criptografado.

4. Feedback: O bloco criptografado resultante é usado como entrada para a criptografia do próximo bloco de dados. Antes da criptografia, o bloco de dados atual é combinado com o bloco criptografado anterior usando a operação XOR.

5. Criptografia dos blocos subsequentes: O processo de feedback é repetido para os blocos subsequentes. Cada bloco de dados é combinado com o bloco criptografado anterior usando a operação XOR, e o resultado é criptografado usando o algoritmo de criptografia de bloco.

6. Bloco criptografado: Após a criptografia de todos os blocos de dados, temos uma sequência de blocos criptografados.

A sequência de blocos criptografados resultantes é a saída final da criptografia usando o modo CBC. Para descriptografar, o processo é realizado em ordem reversa:

1. Vetor de inicialização (IV): O vetor de inicialização original é utilizado como entrada para o primeiro bloco de dados.

2. Descriptografia dos blocos subsequentes: Os blocos criptografados são descriptografados usando o algoritmo de descriptografia de bloco, como o AES. O resultado é combinado com o bloco criptografado anterior usando a operação XOR.

3. Operação XOR: O resultado da descriptografia é combinado com o bloco criptografado anterior usando a operação XOR, obtendo o bloco de dados original.

4. Feedback: O bloco de dados descriptografado é usado como entrada para a descriptografia do próximo bloco de dados. Antes da descriptografia, o bloco de dados atual é combinado com o bloco criptografado anterior usando a operação XOR.

5. Bloco de dados original: Após a descriptografia de todos os blocos de dados, temos a sequência de blocos de dados original.

O modo CBC é amplamente utilizado devido à sua capacidade de fornecer confidencialidade e integridade dos dados. No entanto, é importante mencionar que o modo CBC não fornece autenticação dos dados, o que significa que ele não pode detectar alterações maliciosas nos blocos de dados. Para fornecer autenticação, é necessário adotar mecanismos adicionais, como o uso de códigos de autenticação de mensagem (MAC) ou assinaturas digitais.

## Como funciona o algoritmo de criptografia AES

O algoritmo de criptografia AES (Advanced Encryption Standard) é um dos algoritmos mais amplamente utilizados para criptografar dados. Ele substituiu o antigo algoritmo DES (Data Encryption Standard) devido à sua maior segurança e eficiência. O AES é um algoritmo simétrico de bloco, o que significa que a mesma chave é usada tanto para criptografar quanto para descriptografar os dados. Vamos entender como funciona o algoritmo AES:

1. Tamanho da chave: O AES suporta chaves de 128, 192 e 256 bits. A segurança do algoritmo aumenta proporcionalmente com o tamanho da chave.

2. Divisão em blocos: O texto original a ser criptografado é dividido em blocos de 128 bits (16 bytes). Se o tamanho do texto não for um múltiplo de 128 bits, ele é preenchido com bytes adicionais.

3. Chave de criptografia: Uma chave de criptografia é gerada e usada para criptografar e descriptografar os dados. A chave precisa ser mantida em segredo, pois é a única forma de descriptografar os dados.

4. Rondas: O AES é baseado em um processo chamado "SubBytes", que é aplicado em cada byte do bloco. Esse processo é repetido várias vezes, dependendo do tamanho da chave (10 rondas para chaves de 128 bits, 12 rondas para chaves de 192 bits e 14 rondas para chaves de 256 bits).

5. SubBytes: Nessa etapa, cada byte do bloco é substituído por outro byte da "S-Box", que é uma tabela de substituição pré-definida.

6. ShiftRows: Nessa etapa, as linhas do bloco são permutadas de acordo com um padrão específico.

7. MixColumns: Nessa etapa, as colunas do bloco são misturadas para garantir maior difusão dos dados.

8. AddRoundKey: Nessa etapa, a chave de criptografia é combinada com o bloco por meio de uma operação de XOR bit a bit.

9. Rondas adicionais: As etapas de SubBytes, ShiftRows e MixColumns são repetidas várias vezes, dependendo do tamanho da chave.

10. Última rodada: Na última rodada, a etapa de MixColumns não é aplicada.

11. Bloco criptografado: Após a execução de todas as rondas, o bloco de dados é criptografado.

12. Descriptografia: Para descriptografar, o processo é realizado em ordem reversa. Cada rodada é desfeita aplicando-se as operações inversas nas etapas correspondentes.

O algoritmo AES é altamente seguro e amplamente adotado em várias aplicações, como segurança de rede, armazenamento criptografado, comunicação segura e muito mais. Sua segurança é baseada na complexidade das operações realizadas em cada rodada e no tamanho da chave utilizada.

## Como funciona o algoritmo de criptografia DES

O algoritmo de criptografia DES (Data Encryption Standard) é um dos primeiros e mais amplamente usados algoritmos de criptografia de bloco. No entanto, devido ao avanço da tecnologia e ao aumento da capacidade de processamento dos computadores, o DES foi considerado inseguro e substituído por algoritmos mais fortes, como o AES (Advanced Encryption Standard). No entanto, ainda é útil entender como o DES funciona, já que muitos sistemas legados ainda podem usá-lo.

Aqui está uma explicação de alto nível de como o algoritmo de criptografia DES funciona:

1. Tamanho da chave: O DES usa uma chave de criptografia de 56 bits. A chave é usada tanto para criptografar quanto para descriptografar os dados.

2. Divisão em blocos: O texto original a ser criptografado é dividido em blocos de 64 bits.

3. Permutação inicial (IP): O bloco de dados original é submetido a uma permutação inicial, que reorganiza os bits de acordo com uma tabela predefinida.

4. Rondas de criptografia: O DES usa um total de 16 rondas de criptografia. Cada rodada consiste em várias operações, como substituições não lineares, permutações e operações de XOR com a chave.

5. Função de Feistel: A estrutura do DES é baseada no conceito de uma função de Feistel, que divide o bloco de dados em metades e realiza operações separadas em cada metade. O resultado das operações é combinado com a outra metade antes de prosseguir para a próxima rodada.

6. Subchaves: Antes de cada rodada, a chave de 56 bits é combinada com outras chaves derivadas dela para gerar uma subchave específica para aquela rodada.

7. Rodada final: Após as 16 rondas, uma permutação final (IP-1) é aplicada ao bloco criptografado para obter o texto criptografado final.

8. Descriptografia: Para descriptografar os dados, o processo é realizado em ordem reversa. As subchaves são usadas na ordem inversa, e as operações são desfeitas para obter o texto original.

Apesar de ser um algoritmo pioneiro, o DES é considerado inseguro nos dias de hoje devido ao tamanho curto da chave e aos avanços na capacidade de processamento de computadores. Recomenda-se o uso do AES ou outros algoritmos modernos e mais seguros para proteger os dados sensíveis.

## Como funciona o algoritmo de criptografia 3DES

O algoritmo de criptografia 3DES (Triple Data Encryption Standard), também conhecido como TDEA, é uma variante do algoritmo DES (Data Encryption Standard) que busca aumentar a segurança através da aplicação repetida do DES. O 3DES usa três chaves diferentes para criptografar os dados em três etapas separadas.

Aqui está uma explicação de alto nível de como o algoritmo de criptografia 3DES funciona:

1. Chaves: O 3DES utiliza três chaves distintas, cada uma com 56 bits, totalizando 168 bits no total. Essas chaves são referidas como chave de criptografia 1 (K1), chave de criptografia 2 (K2) e chave de criptografia 3 (K3).

2. Criptografia: O processo de criptografia 3DES ocorre em três etapas:

a) Etapa 1: O bloco de dados original é criptografado usando a chave K1 no algoritmo DES.

b) Etapa 2: O resultado da etapa 1 é descriptografado usando a chave K2 no algoritmo DES.

c) Etapa 3: O resultado da etapa 2 é criptografado novamente usando a chave K3 no algoritmo DES.

3. Descriptografia: Para descriptografar os dados criptografados com 3DES, o processo é realizado em ordem reversa:

a) Etapa 1: O bloco de dados criptografado é descriptografado usando a chave K3 no algoritmo DES.

b) Etapa 2: O resultado da etapa 1 é criptografado usando a chave K2 no algoritmo DES.

c) Etapa 3: O resultado da etapa 2 é descriptografado novamente usando a chave K1 no algoritmo DES.

Ao utilizar três etapas de criptografia e descriptografia, o 3DES aumenta significativamente a segurança em relação ao DES original. No entanto, é importante ressaltar que o 3DES ainda possui algumas limitações devido à sua base no DES, como a chave relativamente curta e o tamanho fixo do bloco de dados. Portanto, em aplicações modernas, é recomendado o uso de algoritmos de criptografia mais fortes, como o AES (Advanced Encryption Standard).

## Como funciona o algoritmo de criptografia Blowfish

O algoritmo de criptografia Blowfish é um algoritmo de criptografia de bloco simétrico, desenvolvido por Bruce Schneier em 1993. Ele é conhecido por sua eficiência e flexibilidade, podendo operar com chaves de tamanho variável, de 32 a 448 bits.

Aqui está uma explicação de alto nível de como o algoritmo de criptografia Blowfish funciona:

1. Expansão de chave: A chave de criptografia é usada para expandir uma matriz de subchaves, que são usadas durante o processo de criptografia. Essa matriz é inicializada com valores pré-calculados e, em seguida, modificada com base na chave.

2. Divisão em blocos: O texto original a ser criptografado é dividido em blocos de tamanho fixo, normalmente 64 bits.

3. Processamento do bloco: Cada bloco de dados passa por uma série de operações para criptografá-lo. O processo consiste em uma série de rondas, onde os dados são misturados usando uma combinação de substituições, permutações e operações matemáticas.

4. Subchaves: Durante cada rodada, uma subchave específica é usada para modificar os dados. As subchaves são selecionadas sequencialmente a partir da matriz de subchaves.

5. Modos de operação: O Blowfish pode ser usado em diferentes modos de operação, como o modo ECB (Electronic Codebook), o modo CBC (Cipher Block Chaining) e outros. Cada modo determina como os blocos de dados são processados e combinados entre si.

6. Descriptografia: Para descriptografar os dados criptografados, o processo é realizado em ordem inversa. As subchaves são usadas na ordem inversa, e as operações são desfeitas para obter o texto original.

O algoritmo Blowfish é amplamente utilizado em aplicações que exigem criptografia eficiente e segura. No entanto, assim como qualquer algoritmo de criptografia, é importante utilizar chaves fortes e seguir as melhores práticas de segurança para garantir a proteção adequada dos dados. Além disso, com o avanço da tecnologia, algoritmos mais modernos, como o AES, são recomendados para aplicações que requerem maior segurança.

## Como funciona o algoritmo de criptografia RC4

O algoritmo de criptografia RC4 (Rivest Cipher 4) é um algoritmo de fluxo de cifra simétrica, o que significa que ele criptografa e descriptografa dados em tempo real à medida que são transmitidos. O RC4 é conhecido por sua simplicidade e eficiência, sendo amplamente utilizado em protocolos de segurança, como o SSL/TLS e o WEP (Wired Equivalent Privacy) para redes sem fio.

Aqui está uma visão geral básica de como o algoritmo de criptografia RC4 funciona:

1. Geração da chave: O RC4 utiliza uma chave de criptografia que pode variar de 40 a 2048 bits de tamanho. A chave é usada para inicializar um vetor de estado interno e gerar uma sequência pseudoaleatória de bytes chamada de "keystream".

2. Inicialização do vetor de estado: O vetor de estado interno, geralmente chamado de S-box, é inicializado com os valores de 0 a 255 em uma ordem específica, com base nos valores dos bytes da chave fornecida.

3. Permutação do vetor de estado: O vetor de estado é permutado várias vezes usando uma combinação de operações de troca de elementos. Esse processo de permutação é chamado de "KSA" (Key Scheduling Algorithm) e embaralha o vetor de estado de acordo com a chave.

4. Geração do keystream: O keystream é gerado pelo algoritmo de "PRGA" (Pseudo-Random Generation Algorithm). Ele utiliza o vetor de estado permutado e gera uma sequência pseudoaleatória de bytes, que é usada para combinar com os dados a serem criptografados ou descriptografados.

5. Combinação com os dados: O keystream gerado é combinado com os dados por meio de uma operação de OU exclusivo (XOR), bit a bit. Essa operação combina cada byte do keystream com o byte correspondente dos dados, produzindo os dados criptografados ou descriptografados.

É importante mencionar que o algoritmo RC4 foi encontrado com algumas vulnerabilidades ao longo dos anos, principalmente no uso incorreto ou fraco das chaves. Como resultado, o RC4 é geralmente considerado inseguro para uso em criptografia forte. Recomenda-se utilizar algoritmos mais modernos e seguros, como o AES (Advanced Encryption Standard), em vez do RC4.

## Como funciona o algoritmo de criptografia RC5

O algoritmo de criptografia RC5 (Rivest Cipher 5) é um algoritmo de criptografia de bloco simétrico. Foi proposto por Ronald Rivest em 1994 e é uma evolução do algoritmo RC4. O RC5 é conhecido por sua simplicidade e flexibilidade, permitindo a variação do tamanho do bloco, a quantidade de rodadas e o tamanho da chave.

Aqui está uma visão geral básica de como o algoritmo de criptografia RC5 funciona:

1. Tamanho do bloco e chave: O RC5 permite que o tamanho do bloco e o tamanho da chave sejam definidos. O tamanho do bloco é geralmente de 32 ou 64 bits, e o tamanho da chave pode variar de 0 a 2040 bits.

2. Expandindo a chave: A chave fornecida é processada por um algoritmo de expansão de chave para gerar uma série de subchaves. Essas subchaves são usadas nas rodadas subsequentes do algoritmo.

3. Operações básicas: O RC5 usa duas operações básicas: adição modular e rotação bit a bit. A adição modular é usada para combinar a chave e os blocos de dados com as subchaves. A rotação bit a bit é usada para manipular os dados em diferentes rodadas do algoritmo.

4. Rodadas: O algoritmo RC5 executa uma série de rodadas, onde os blocos de dados são manipulados repetidamente. Cada rodada envolve operações de adição modular, rotação bit a bit e combinação com subchaves.

5. Modos de operação: O RC5 pode ser usado em diferentes modos de operação, como modo de bloco único (ECB), modo de feedback de cifra (CFB), modo de retroalimentação em cadeia (CBC), entre outros. Esses modos determinam como os blocos de dados são processados e como a criptografia é aplicada aos dados.

É importante mencionar que, embora o algoritmo RC5 seja considerado seguro, ele não é tão amplamente adotado quanto outros algoritmos de criptografia, como o AES (Advanced Encryption Standard). O AES é atualmente considerado o padrão de criptografia mais forte e amplamente usado.

## Diferenças entre a rede de FEISTEL, disseminada pelo DES, e o algoritmo de RJINDAEL, utilizada pelo AES

A rede de Feistel é uma estrutura de cifra que foi amplamente utilizada no algoritmo DES (Data Encryption Standard), enquanto o algoritmo Rijndael é a base do AES (Advanced Encryption Standard). Embora ambos sejam algoritmos de criptografia simétrica, existem diferenças significativas entre eles. Aqui estão algumas das principais diferenças:

1. Estrutura: A rede de Feistel é uma estrutura de cifra iterativa que divide o bloco de dados em metades e aplica uma série de rodadas de transformações ao longo dessas metades. Cada rodada envolve operações de substituição, permutação e combinação das metades. Por outro lado, o algoritmo Rijndael (usado no AES) é uma estrutura de cifra de bloco que opera em blocos de dados de tamanho fixo, geralmente 128 bits, e envolve um conjunto de transformações lineares e não lineares.

2. Tamanho da chave e dos blocos: O DES tem um tamanho de bloco fixo de 64 bits e permite apenas chaves de 56 bits de comprimento, o que o torna vulnerável a ataques de força bruta. Por outro lado, o AES (Rijndael) suporta tamanhos de bloco de 128, 192 e 256 bits, e chaves com comprimentos de 128, 192 e 256 bits, oferecendo maior segurança e flexibilidade.

3. Número de rodadas: O DES consiste em 16 rodadas de transformações para criptografar ou descriptografar dados. O número de rodadas foi considerado adequado na época em que o DES foi desenvolvido, mas com o avanço da tecnologia, tornou-se suscetível a ataques mais sofisticados. Por outro lado, o AES possui um número variável de rodadas, dependendo do tamanho da chave e do tamanho do bloco escolhidos. Para chaves de 128 bits, o AES usa 10 rodadas, para chaves de 192 bits usa 12 rodadas e para chaves de 256 bits usa 14 rodadas. O aumento do número de rodadas aumenta a segurança do algoritmo.

4. Segurança: O DES, devido ao tamanho limitado da chave e ao número fixo de rodadas, foi considerado relativamente inseguro com o passar do tempo. Foram desenvolvidos ataques eficientes contra o DES, o que levou ao desenvolvimento do AES. O AES (Rijndael) é considerado altamente seguro e resistente a ataques conhecidos até o momento, desde que as chaves sejam suficientemente longas.

Em resumo, embora o DES e o AES sejam algoritmos de criptografia simétrica, o AES (baseado no algoritmo Rijndael) oferece maior segurança, flexibilidade e capacidade de resistir a ataques em comparação com o DES (baseado na rede de Feistel). Por essas razões, o AES é amplamente utilizado como o padrão de criptografia em muitas aplicações e sistemas atualmente.
