# Mecanismos de segurança - Criptografia

Criptografia é o processo de transformar informações legíveis em uma forma ilegível, chamada de texto cifrado, por meio do uso de algoritmos matemáticos. Essa técnica é amplamente utilizada para garantir a confidencialidade dos dados, protegendo-os contra acesso não autorizado.
Existem dois principais tipos de criptografia:

1. Criptografia simétrica: Nesse tipo de criptografia, uma única chave é usada tanto para criptografar quanto para descriptografar os dados. A mesma chave é compartilhada entre o remetente e o destinatário da mensagem. A criptografia simétrica é mais rápida e eficiente, mas requer que a chave seja mantida em segredo. Alguns algoritmos simétricos comuns são o AES (Advanced Encryption Standard) e o DES (Data Encryption Standard).

2. Criptografia assimétrica (ou de chave pública): Nesse tipo de criptografia, são usados dois tipos de chaves: uma chave pública e uma chave privada. A chave pública é usada para criptografar os dados, enquanto a chave privada é usada para descriptografá-los. As chaves são geradas em pares e são matematicamente relacionadas, mas é computacionalmente difícil derivar a chave privada a partir da chave pública. Isso permite que a chave pública seja distribuída livremente, enquanto a chave privada é mantida em sigilo. A criptografia assimétrica é mais segura, mas também é mais lenta e computacionalmente intensiva. Alguns algoritmos assimétricos populares são o RSA e o ECC (Elliptic Curve Cryptography).

Além disso, existem várias aplicações da criptografia em diferentes cenários:

1. Comunicação segura na Internet: A criptografia é usada para proteger as comunicações em redes, como a Internet. Protocolos como o SSL (Secure Sockets Layer) e o TLS (Transport Layer Security) são usados para criptografar as informações transmitidas entre um servidor e um cliente, garantindo que os dados não possam ser interceptados ou lidos por terceiros.

2. Armazenamento de dados sensíveis: A criptografia é aplicada ao armazenamento de dados em dispositivos, como discos rígidos, dispositivos USB e serviços de armazenamento em nuvem. Isso garante que, mesmo se o dispositivo for perdido ou roubado, os dados permaneçam protegidos.

3. Autenticação: A criptografia também é usada para fins de autenticação, por meio do uso de assinaturas digitais. Uma assinatura digital é uma sequência criptografada de dados que comprova a autenticidade e integridade de uma mensagem. Isso permite que o receptor verifique se a mensagem não foi alterada e se realmente foi enviada pelo remetente esperado.

A criptografia desempenha um papel fundamental na segurança da informação, fornecendo uma camada de proteção essencial para a confidencialidade dos dados. No entanto, é importante ressaltar que a criptografia por si só não é suficiente para garantir a segurança completa de um sistema. Outros mecanismos de segurança, como autenticação, controle de acesso e proteção contra malware, também devem ser implementados em conjunto com a criptografia para obter um ambiente seguro

