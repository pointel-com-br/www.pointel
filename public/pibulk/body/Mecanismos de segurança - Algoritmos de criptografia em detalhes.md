# Mecanismos de segurança - Algoritmos de criptografia em detalhes

Existem vários algoritmos de criptografia disponíveis, cada um com seus próprios princípios matemáticos e propriedades de segurança. Aqui estão alguns dos algoritmos de criptografia mais comuns em detalhes:

1. AES (Advanced Encryption Standard):
- Descrição: O AES é um dos algoritmos de criptografia mais amplamente adotados e é usado para criptografar e descriptografar dados. Ele opera em blocos de dados fixos e suporta tamanhos de chave de 128, 192 e 256 bits.
- Funcionamento: O AES utiliza uma série de transformações chamadas SubBytes, ShiftRows, MixColumns e AddRoundKey em várias rodadas para transformar os dados de entrada em texto cifrado. Essas mesmas transformações são aplicadas na ordem inversa para descriptografar os dados.

2. RSA (Rivest, Shamir e Adleman):
- Descrição: O RSA é um algoritmo de criptografia assimétrica amplamente utilizado para criptografia de chave pública e assinaturas digitais.
- Funcionamento: O RSA é baseado na dificuldade de fatoração de números grandes. Ele envolve a geração de um par de chaves: uma chave pública para criptografar os dados e uma chave privada correspondente para descriptografá-los. A segurança do RSA está fundamentada na dificuldade computacional de fatorar o produto de dois números primos grandes.

3. ECC (Elliptic Curve Cryptography):

- Descrição: A ECC é um tipo de criptografia assimétrica que utiliza a matemática das curvas elípticas para criptografar e descriptografar dados.

- Funcionamento: A ECC baseia-se na dificuldade computacional de resolver o problema do logaritmo discreto em uma curva elíptica. Ela envolve a geração de um par de chaves: uma chave pública para criptografar os dados e uma chave privada correspondente para descriptografá-los. A ECC oferece um nível de segurança semelhante ao RSA, mas com tamanhos de chave menores, tornando-a eficiente em termos de recursos computacionais.

4. DES (Data Encryption Standard):

- Descrição: O DES é um algoritmo de criptografia simétrica mais antigo, amplamente usado no passado, mas atualmente considerado menos seguro devido ao seu tamanho de chave curto.

- Funcionamento: O DES opera em blocos de dados de 64 bits e usa uma chave de 56 bits. Ele aplica uma série de transformações, incluindo permutações, substituições e deslocamentos, em várias rodadas para criptografar e descriptografar os dados.

5. Blowfish:

- Descrição: O Blowfish é um algoritmo de criptografia simétrica rápido e flexível, projetado para substituir o DES.

- Funcionamento: O Blowfish opera em blocos de dados de tamanho variável e suporta chaves de comprimento entre 32 e 448 bits. Ele usa uma série de substituições, permutações e operações XOR em várias rodadas para criptografar e descriptografar os dados.
É importante mencionar que a segurança de um algoritmo de criptografia depende não apenas da sua robustez matemática, mas também da implementação correta e da proteção adequada das chaves. Além disso, é sempre recomendável usar algoritmos atualizados e seguros, que sejam amplamente aceitos e revisados pela comunidade de criptografia.

