# Servidor web e de aplicação - Nginx

O Nginx é um servidor web e proxy reverso de alto desempenho. Ele foi criado para resolver problemas de escalabilidade e desempenho encontrados em servidores web tradicionais. O Nginx é conhecido por sua eficiência, baixo consumo de recursos e capacidade de lidar com um grande número de solicitações simultâneas. Aqui estão algumas informações importantes sobre o Nginx:

1. Servidor web leve e eficiente: O Nginx foi projetado para ser leve e eficiente em termos de recursos. Ele consome menos memória em comparação com outros servidores web tradicionais, o que o torna adequado para lidar com um grande número de solicitações com eficiência.

2. Proxy reverso: Uma das principais funcionalidades do Nginx é atuar como um proxy reverso. Ele pode redirecionar solicitações de clientes para outros servidores web ou aplicativos, fornecendo balanceamento de carga e melhorando o desempenho e a disponibilidade do serviço.

3. Escalabilidade: O Nginx foi projetado para ser altamente escalável. Ele pode lidar com um grande número de solicitações simultâneas usando um modelo de processamento assíncrono e não bloqueante. Isso permite que ele seja eficiente mesmo em cargas de trabalho intensas.

4. Balanceamento de carga: O Nginx tem recursos embutidos para balanceamento de carga. Ele pode distribuir as solicitações entre vários servidores de aplicação, ajudando a otimizar o desempenho e a disponibilidade dos aplicativos.

5. SSL/TLS e segurança: O Nginx oferece suporte a criptografia SSL/TLS para comunicação segura entre o servidor e os clientes. Ele pode atuar como um terminador SSL/TLS, lidando com a criptografia e decodificação das solicitações. Além disso, o Nginx possui recursos de segurança, como limitação de taxa de solicitações, prevenção de ataques DDoS e suporte a regras de firewall.

6. Configuração flexível: O Nginx possui uma sintaxe de configuração flexível e poderosa. Isso permite que os administradores personalizem o comportamento do servidor de acordo com as necessidades específicas. Ele também oferece suporte a várias extensões e módulos para adicionar funcionalidades extras.

O Nginx é amplamente utilizado como servidor web e proxy reverso em uma variedade de cenários, desde hospedagem de sites estáticos até aplicativos da web de alto desempenho. Sua combinação de leveza, desempenho e recursos avançados o torna uma escolha popular para muitos desenvolvedores e administradores de sistemas.

# Servidor web e de aplicação - Nginx - Configuração HTTPS.

Para configurar o HTTPS no servidor web Nginx, você precisa seguir alguns passos. Aqui está uma breve descrição de como configurar o HTTPS usando o Nginx:

1. Certificado SSL/TLS: Assim como no Apache, o primeiro passo é obter um certificado SSL/TLS válido. Você pode adquirir um certificado de uma autoridade de certificação confiável ou gerar um certificado autoassinado para ambientes de desenvolvimento ou teste.

2. Configurar o arquivo de configuração: Abra o arquivo de configuração do Nginx para o seu site ou virtual host. O arquivo de configuração geralmente está localizado no diretório `/etc/nginx/conf.d/` ou `/etc/nginx/sites-available/`. Certifique-se de que o arquivo contenha as seguintes linhas ou adicione-as, se necessário:

```
server {
listen 443 ssl;
server_name seu_dominio.com;

ssl_certificate /caminho/para/o/certificado.crt;
ssl_certificate_key /caminho/para/a/chave_privada.key;

# Configurações adicionais
location / {
# Configurações adicionais para lidar com as solicitações
}
}
```

Lembre-se de substituir `seu_dominio.com` pelo seu próprio domínio e os caminhos para o certificado e a chave privada.

3. Configurar as diretivas SSL: Além das configurações básicas no arquivo de configuração, você também pode adicionar diretivas SSL adicionais para aprimorar a segurança e o desempenho. Alguns exemplos comuns incluem:

- `ssl_protocols`: Define os protocolos SSL/TLS permitidos, como TLSv1.2 ou TLSv1.3.
- `ssl_ciphers`: Define os algoritmos de criptografia permitidos.
- `ssl_prefer_server_ciphers`: Especifica se o servidor deve preferir os algoritmos de criptografia do servidor ou do cliente.

4. Reiniciar o Nginx: Após fazer as alterações no arquivo de configuração, reinicie o servidor Nginx para aplicar as configurações. Use o comando `sudo service nginx restart`.

5. Verificar a configuração: Verifique se a configuração está correta reiniciando o Nginx e verificando os arquivos de log. Se houver erros, os logs geralmente fornecem informações úteis para solucionar problemas.

Após seguir essas etapas, seu servidor Nginx estará configurado para usar o HTTPS. Certifique-se de que as portas 443 (HTTPS) estejam abertas em seu firewall e que seu domínio esteja apontando para o IP correto do servidor.

# Servidor web e de aplicação - Nginx - Configurar como balanceador de carga HTTP.

Para configurar o Nginx como um balanceador de carga HTTP, você pode usar o recurso de proxy reverso do Nginx. Aqui está uma breve descrição de como configurar o Nginx como um balanceador de carga:

1. Configurar os backends: Primeiro, você precisa configurar os backends, ou seja, os servidores que receberão as solicitações do balanceador de carga. Abra o arquivo de configuração do Nginx e adicione as seguintes linhas para cada backend:

```
upstream backend_cluster {
server ip_do_backend1:porta;
server ip_do_backend2:porta;
# Adicione mais servidores conforme necessário
}
```

Certifique-se de substituir `ip_do_backend1` e `ip_do_backend2` pelos endereços IP dos seus servidores backend e `porta` pela porta em que eles estão ouvindo as solicitações.

2. Configurar o balanceador de carga: Agora, você precisa configurar o balanceador de carga propriamente dito. Adicione as seguintes linhas ao seu arquivo de configuração:

```
server {
listen 80;
server_name seu_dominio.com;

location / {
proxy_pass http://backend_cluster;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
}
}
```

Lembre-se de substituir `seu_dominio.com` pelo seu próprio domínio.

3. Reiniciar o Nginx: Após fazer as alterações no arquivo de configuração, reinicie o servidor Nginx para aplicar as configurações. Use o comando `sudo service nginx restart`.

4. Verificar a configuração: Verifique se a configuração está correta reiniciando o Nginx e verificando os arquivos de log. Além disso, você pode testar o balanceador de carga enviando solicitações HTTP e verificando se elas estão sendo distribuídas entre os servidores backend.

Você também pode ajustar as configurações adicionais do balanceador de carga, como o algoritmo de balanceamento de carga, o controle de sessão e as configurações de proxy reverso, conforme necessário. O Nginx oferece uma variedade de recursos poderosos para personalizar o comportamento do balanceador de carga.

Essas etapas ajudarão você a configurar o Nginx como um balanceador de carga HTTP. Certifique-se de ajustar as configurações de acordo com suas necessidades específicas e considere a adoção de práticas recomendadas de segurança e desempenho.
alterações no arquivo de configuração, reinicie o servidor Nginx para aplicar as configurações. Use o comando `sudo service nginx restart`.

4. Verificar a configuração: Verifique se a configuração está correta reiniciando o Nginx e verificando os arquivos de log. Além disso, você pode testar o balanceador de carga enviando solicitações HTTP e verificando se elas estão sendo distribuídas entre os servidores backend.

Você também pode ajustar as configurações adicionais do balanceador de carga, como o algoritmo de balanceamento de carga, o controle de sessão e as configurações de proxy reverso, conforme necessário. O Nginx oferece uma variedade de recursos poderosos para personalizações.

# Parâmetros que o servidor nginx aceita com -s.

No contexto do servidor web Nginx, o parâmetro `-s` é usado para enviar comandos para o processo principal do Nginx. Ele permite controlar o comportamento do servidor sem precisar reiniciar ou recarregar a configuração completa.

O parâmetro `-s` deve ser seguido por um comando específico. Abaixo estão os comandos suportados pelo Nginx:

1. `stop`: Encerra o processo principal do Nginx imediatamente, sem esperar pelas conexões ativas serem concluídas. Este comando é mais abrupto do que o comando `quit`.

2. `quit`: Encerra o processo principal do Nginx de forma limpa, permitindo que as conexões ativas sejam concluídas antes de encerrar o servidor.

3. `reload`: Recarrega a configuração do Nginx sem interromper as conexões ativas. Esse comando é útil quando você faz alterações na configuração do servidor e deseja que as alterações entrem em vigor sem reiniciar completamente o servidor.

4. `reopen`: Reabre os arquivos de log do Nginx. Isso é útil quando você deseja que o Nginx comece a escrever em novos arquivos de log, por exemplo, após fazer log rotate dos arquivos antigos.

Portanto, o parâmetro `-s` do Nginx é seguido por um desses comandos para controlar o comportamento do servidor. Por exemplo, para recarregar a configuração do Nginx, você pode usar o seguinte comando:

```bash
nginx -s reload
```

Certifique-se de ter permissões suficientes para enviar comandos para o processo principal do Nginx, pois geralmente é necessário executar o comando como usuário root ou usar o sudo.

# Parâmetros de linha de comando.

O nginx suporta os seguintes parâmetros de linha de comando:

-? | -h — ajuda de impressão para parâmetros de linha de comando.

-c file — use uma configuração alternativa fileem vez de um arquivo padrão.

-e file — use um log de erro alternativo filepara armazenar o log em vez de um arquivo padrão (1.19.5). O valor especial stderrseleciona o arquivo de erro padrão.
-g directives — definir diretivas de configuração global , por exemplo,
nginx -g "pid /var/run/nginx.pid; worker_processes `sysctl -n hw.ncpu`;"

-p prefix — defina o prefixo do caminho nginx, ou seja, um diretório que manterá os arquivos do servidor (o valor padrão é /usr/local/nginx).

-q — suprimir mensagens sem erro durante o teste de configuração.

-s signal — enviar um sinal para o processo mestre. O sinal do argumento pode ser um dos seguintes:

stop - desligar rapidamente quit - desligar graciosamente reload — recarregar a configuração, iniciar o novo processo de trabalho com uma nova configuração, encerrar processos de trabalho antigos com elegância.
reopen — reabrir arquivos de log

-t — teste o arquivo de configuração: o nginx verifica a configuração quanto à sintaxe correta e, em seguida, tenta abrir os arquivos referidos na configuração.

-T — o mesmo que -t, mas adicionalmente despeja arquivos de configuração na saída padrão (1.9.2).

-v — imprima a versão do nginx.

-V — imprima a versão do nginx, a versão do compilador e configure os parâmetros.

# Métodos de balanceamento de carga no Nginx.

O Nginx é um servidor web de alto desempenho e pode ser usado como um balanceador de carga para distribuir o tráfego entre vários servidores backend. Existem diferentes métodos de balanceamento de carga disponíveis no Nginx, incluindo:

1. Balanceamento de carga baseado em round-robin: O Nginx distribui as solicitações de forma igualitária entre os servidores backend. Cada solicitação subsequente é enviada para o próximo servidor na lista, seguindo uma ordem circular.

Exemplo de configuração:
```
http {
    upstream backend {
        server backend1.example.com;
        server backend2.example.com;
        server backend3.example.com;
    }

    server {
        listen 80;
        location / {
            proxy_pass http://backend;
        }
    }
}
```

2. Balanceamento de carga ponderado: Neste método, você pode atribuir um peso a cada servidor backend com base em sua capacidade de lidar com solicitações. O Nginx distribuirá as solicitações proporcionalmente aos pesos atribuídos.

Exemplo de configuração:
```
http {
    upstream backend {
        server backend1.example.com weight=3;
        server backend2.example.com weight=2;
        server backend3.example.com weight=1;
    }

    server {
        listen 80;
        location / {
            proxy_pass http://backend;
        }
    }
}
```

3. Balanceamento de carga baseado em IP hash: O Nginx usa o endereço IP do cliente para calcular um hash e, em seguida, envia solicitações subsequentes do mesmo cliente para o mesmo servidor backend. Isso é útil quando você deseja manter a persistência de sessão para um cliente específico.

Exemplo de configuração:
```
http {
    upstream backend {
        ip_hash;
        server backend1.example.com;
        server backend2.example.com;
        server backend3.example.com;
    }

    server {
        listen 80;
        location / {
            proxy_pass http://backend;
        }
    }
}
```

4. Balanceamento de carga baseado em algoritmos mais avançados: O Nginx também suporta outros métodos de balanceamento de carga, como least_conn (encaminha solicitações para o servidor com a menor quantidade de conexões ativas), ip_hash (balanceamento baseado em hash de endereço IP), entre outros.

Exemplo de configuração:

```
http {
    upstream backend {
        least_conn;
        server backend1.example.com;
        server backend2.example.com;
        server backend3.example.com;
    }

    server {
        listen 80;
        location / {
            proxy_pass http://backend;
        }
    }
}
```

Esses são apenas alguns exemplos de métodos de balanceamento de carga disponíveis no Nginx. A escolha do método adequado depende dos requisitos e da infraestrutura do seu aplicativo. Você pode encontrar mais detalhes na documentação oficial do Nginx.

# Funcionamento do worker_processes e do worker_connections no Nginx.

No Nginx, as configurações `worker_processes` e `worker_connections` controlam a maneira como os processos e conexões são gerenciados pelo servidor.

1. `worker_processes`:
- O `worker_processes` define o número de processos de trabalho (workers) que o servidor Nginx usará para processar as solicitações. Cada processo de trabalho é responsável por lidar com as conexões de entrada e processar as solicitações.
- O valor padrão é geralmente definido como o número de núcleos do processador disponíveis no servidor. O Nginx pode aproveitar os recursos do sistema, distribuindo o trabalho entre vários processos de trabalho.
- É recomendado ajustar esse valor com base no hardware do servidor e na carga esperada. Um valor muito baixo pode limitar o desempenho, enquanto um valor muito alto pode levar a um consumo excessivo de recursos.
- Exemplo de configuração:
     ```
     worker_processes 4;
```

2. `worker_connections`:
- O `worker_connections` define o número máximo de conexões simultâneas que um processo de trabalho pode manipular. Isso inclui conexões HTTP, HTTPS, conexões de proxy, entre outras.
- Cada solicitação HTTP ou conexão estabelecida com o servidor Nginx consome uma conexão do processo de trabalho.
- É importante definir um valor adequado para `worker_connections` para lidar com a carga esperada. Se o valor for muito baixo, pode ocorrer a recusa de conexões quando o limite for atingido.
- É recomendado calcular o valor máximo possível com base nos recursos do servidor e nos requisitos de desempenho. Uma fórmula comum é multiplicar o número de `worker_processes` pelo valor desejado de `worker_connections`.
- Exemplo de configuração:
     ```
     events {
         worker_connections 1024;
     }
```

É importante ajustar essas configurações de acordo com o ambiente e a carga esperada do seu servidor Nginx. Monitorar o desempenho do servidor e realizar testes de carga pode ajudar a determinar os valores ideais para obter o melhor desempenho e a capacidade de lidar com a carga de solicitações de forma eficiente.

# Escolhendo um Método de Balanceamento de Carga.

O NGINX Open Source suporta quatro métodos de balanceamento de carga, e o NGINX Plus adiciona mais dois métodos:

1. Round Robin - As solicitações são distribuídas igualmente entre os servidores, levando em consideração os pesos dos servidores. Este método é usado por padrão (não há diretiva para ativá-lo):

    ```nginx
    upstream backend {
       # nenhum método de balanceamento de carga é especificado para o Round Robin
       server backend1.example.com;
       server backend2.example.com;
    }
```

2. Least Connections - Uma solicitação é enviada para o servidor com o menor número de conexões ativas, novamente levando em consideração os pesos dos servidores:

    ```nginx
    upstream backend {
        least_conn;
        server backend1.example.com;
        server backend2.example.com;
    }
```

3. IP Hash - O servidor para o qual uma solicitação é enviada é determinado pelo endereço IP do cliente. Nesse caso, os três primeiros octetos do endereço IPv4 ou o endereço IPv6 completo são usados para calcular o valor de hash. O método garante que solicitações do mesmo endereço sejam enviadas para o mesmo servidor, a menos que ele não esteja disponível.

    ```nginx
    upstream backend {
        ip_hash;
        server backend1.example.com;
        server backend2.example.com;
    }
```

Se um dos servidores precisa ser temporariamente removido da rota de balanceamento de carga, ele pode ser marcado com o parâmetro `down` para preservar o hash atual dos endereços IP dos clientes. As solicitações que seriam processadas por esse servidor são automaticamente enviadas para o próximo servidor do grupo:

    ```nginx
    upstream backend {
        server backend1.example.com;
        server backend2.example.com;
        server backend3.example.com down;
    }
```

4. Generic Hash - O servidor para o qual uma solicitação é enviada é determinado por uma chave definida pelo usuário, que pode ser uma sequência de texto, uma variável ou uma combinação. Por exemplo, a chave pode ser um par de endereço IP de origem e porta, ou um URI, como neste exemplo:

    ```nginx
    upstream backend {
        hash $request_uri consistent;
        server backend1.example.com;
        server backend2.example.com;
    }
```

O parâmetro opcional `consistent` para a diretiva `hash` habilita o balanceamento de carga hash consistente ketama. As solicitações são distribuídas igualmente entre todos os servidores upstream com base no valor de chave hash definido pelo usuário. Se um servidor upstream for adicionado ou removido de um grupo upstream, apenas algumas chaves serão remapeadas, o que minimiza as perdas de cache no caso de servidores de cache de balanceamento de carga ou outras aplicações que acumulam estado.

5. Least Time (somente NGINX Plus) - Para cada solicitação, o NGINX Plus seleciona o servidor com a menor latência média e o menor número de conexões ativas, em que a menor latência média é calculada com base nos seguintes parâmetros da diretiva `least_time`:

- `header` - Tempo para receber o primeiro byte do servidor
- `last_byte` - Tempo para receber a resposta completa do servidor

- `last_byte inflight` - Tempo para receber a resposta completa do servidor, levando em consideração solicitações incompletas

    ```nginx
    upstream backend {
        least_time header;
        server backend1.example.com;
        server backend2.example.com;
    }
```

6. Random - Cada solicitação é enviada para um servidor selecionado aleatoriamente. Se o parâmetro `two` for especificado, primeiro o NGINX seleciona aleatoriamente dois servidores levando em consideração os pesos dos servidores e, em seguida, escolhe um desses servidores usando o método especificado:

- `least_conn` - O menor número de conexões ativas
- `least_time=header` (NGINX Plus) - O menor tempo médio para receber o cabeçalho de resposta do servidor (`$upstream_header_time`)
- `least_time=last_byte` (NGINX Plus) - O menor tempo médio para receber a resposta completa do servidor (`$upstream_response_time`)

    ```nginx
    upstream backend {
        random two least_time=last_byte;
        server backend1.example.com;
        server backend2.example.com;
        server backend3.example.com;
        server backend4.example.com;
    }
```

O método de balanceamento de carga **Random** deve ser usado para ambientes distribuídos em que vários balanceadores de carga estão enviando solicitações para o mesmo conjunto de servidores backend. Para ambientes em que o balanceador de carga tem uma visão completa de todas as solicitações, use outros métodos de balanceamento de carga, como round robin, least connections e least time.

> **Observação:** Ao configurar qualquer método que não seja o Round Robin, coloque a diretiva correspondente (`hash`, `ip_hash`, `least_conn`, `least_time` ou `random`) acima da lista de diretivas `server` no bloco `upstream{}`.
