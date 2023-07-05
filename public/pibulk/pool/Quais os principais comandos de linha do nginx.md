# Quais os principais comandos de linha do nginx?

O Nginx é um servidor web e proxy reverso popular, amplamente utilizado em servidores web. Ele também possui comandos de linha para controlar e gerenciar seu funcionamento. Abaixo estão alguns dos principais comandos de linha do Nginx:

1. **nginx**: Inicia o servidor Nginx.
   Exemplo: `nginx`

2. **nginx -s stop**: Interrompe o servidor Nginx de forma imediata.
   Exemplo: `nginx -s stop`

3. **nginx -s quit**: Encerra o servidor Nginx de forma suave, permitindo que as conexões ativas sejam concluídas antes de fechar.
   Exemplo: `nginx -s quit`

4. **nginx -s reload**: Recarrega a configuração do servidor Nginx sem interromper as conexões ativas.
   Exemplo: `nginx -s reload`

5. **nginx -s reopen**: Reabre os arquivos de log do Nginx.
   Exemplo: `nginx -s reopen`

6. **nginx -t**: Verifica a sintaxe e a validade da configuração do Nginx.
   Exemplo: `nginx -t`

7. **nginx -v**: Exibe a versão do servidor Nginx instalada.
   Exemplo: `nginx -v`

Esses são apenas alguns dos principais comandos de linha do Nginx. Você pode obter mais informações e explorar outros comandos executando `nginx -h` ou consultando a documentação oficial do Nginx.
