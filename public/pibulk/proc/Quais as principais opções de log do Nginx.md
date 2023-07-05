# Quais as principais opções de log do Nginx?

O Nginx oferece diversas opções de log para registrar e monitorar atividades relacionadas ao servidor. Aqui estão algumas das principais opções de log disponíveis no Nginx:

1. **Access Log**: O arquivo de log de acesso registra informações sobre todas as solicitações recebidas pelo servidor Nginx, incluindo o endereço IP do cliente, a data e hora da solicitação, o método HTTP usado, o URL solicitado, o código de status da resposta e outras informações relevantes. O arquivo de log de acesso é configurado usando a diretiva `access_log`.

2. **Error Log**: O arquivo de log de erro registra mensagens de erro e avisos relacionados ao servidor Nginx. Isso inclui erros de configuração, erros de syntax, erros de aplicativo, falhas de autenticação, problemas de conexão, entre outros. O arquivo de log de erro é configurado usando a diretiva `error_log`.

3. **Log Format**: O Nginx permite que você defina formatos personalizados para os logs de acesso. Você pode especificar as informações que deseja registrar, como o endereço IP do cliente, a data e hora, o método HTTP, o URL solicitado, o código de status da resposta e outras informações, e definir um formato personalizado usando as variáveis pré-definidas pelo Nginx. Isso é configurado usando a diretiva `log_format`.

4. **Buffered Logging**: O Nginx oferece suporte a log buffering, o que significa que as informações de log são armazenadas temporariamente em um buffer antes de serem gravadas no disco. Isso ajuda a melhorar o desempenho do servidor, reduzindo a quantidade de E/S de disco necessária para gravar os logs. O buffering é controlado pela diretiva `log_buffer_size`.

5. **Log Rotation**: O Nginx não possui uma funcionalidade interna de rotação de log como o Apache, mas é comum usar utilitários externos, como o `logrotate`, para fazer a rotação dos arquivos de log do Nginx. Isso permite que você mantenha um número limitado de arquivos de log e os comprima ou arquive automaticamente após um determinado período de tempo.

Essas são apenas algumas das principais opções de log disponíveis no Nginx. O servidor Nginx oferece flexibilidade para configurar e personalizar os registros de acordo com suas necessidades específicas. Consulte a documentação oficial do Nginx para obter informações mais detalhadas sobre as opções de log disponíveis.
