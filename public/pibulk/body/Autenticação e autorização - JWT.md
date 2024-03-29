# Autenticação e autorização - JWT

JWT (JSON Web Token) é um padrão aberto (RFC 7519) para a criação de tokens de acesso que podem ser usados para autenticação e compartilhamento de informações entre diferentes partes de um sistema. É uma forma compacta e autossuficiente de representar informações em formato JSON, assinadas digitalmente para garantir sua integridade.
Um JWT consiste em três partes separadas por pontos (.), que são:

1. Header (Cabeçalho): Contém informações sobre o tipo de token e o algoritmo de assinatura usado. Geralmente, o tipo de token é "JWT" e o algoritmo de assinatura pode ser, por exemplo, HMAC SHA256 ou RSA.
Exemplo de cabeçalho JWT:

{
"alg": "HS256",
"typ": "JWT"
}

2. Payload (Carga): É onde são inseridas as informações adicionais, conhecidas como "claims", que descrevem a entidade (usuário, dispositivo etc.) e fornecem dados adicionais relevantes. Existem três tipos de claims em um JWT:

- Registered Claims (Claims Registrados): São claims pré-definidos e padronizados, como "iss" (emissor), "sub" (sujeito), "exp" (data de expiração) e "iat" (data de emissão), entre outros. Esses claims têm um significado específico e devem ser usados de acordo com as convenções definidas.

- Public Claims (Claims Públicos): São claims definidos pelo desenvolvedor para atender às necessidades específicas do aplicativo ou sistema. Eles não entram em conflito com os claims registrados.

- Private Claims (Claims Privados): São claims personalizados que são usados para compartilhar informações específicas entre as partes envolvidas. Esses claims não devem entrar em conflito com os claims registrados ou públicos.
Exemplo de payload JWT:

{
"sub": "1234567890",
"name": "John Doe",
"iat": 1516239022
}

3. Signature (Assinatura): É a parte final do JWT, que é usada para verificar a integridade do token. A assinatura é criada combinando o cabeçalho codificado, a carga codificada, uma chave secreta (no caso de algoritmos de assinatura simétricos) ou uma chave pública/privada (no caso de algoritmos de assinatura assimétricos). A assinatura é usada para verificar se o token foi modificado durante a transmissão ou armazenamento.
O processo geral de uso de um JWT envolve a criação do token, sua transmissão entre as partes envolvidas e a verificação da assinatura para garantir sua autenticidade e integridade. Uma vez que a assinatura seja verificada com sucesso, as informações contidas no payload podem ser consideradas confiáveis.
Os JWTs são amplamente usados em aplicações web e APIs como forma de autenticação e autorização. Eles são especialmente úteis em cenários de microserviços e comunicações entre diferentes sistemas, permitindo que informações sejam compartilhadas de forma segura e confiável.

É importante observar que, ao usar JWTs, é necessário proteger a chave secreta ou as chaves públicas/privadas usadas para a assinatura, a fim de evitar a falsificação de tokens ou acesso não autorizado. Além disso, é necessário garantir que os tokens JWT tenham uma vida útil limitada e sejam revogados quando necessário, para evitar o uso indevido de tokens expirados ou comprometidos.
