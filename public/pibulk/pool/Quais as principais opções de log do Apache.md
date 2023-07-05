# Quais as principais opções de log do Apache

O Apache HTTP Server oferece uma variedade de opções de log para registrar e monitorar atividades relacionadas ao servidor. Aqui estão algumas das principais opções de log disponíveis:

1. **Access Log**: O arquivo de log de acesso registra informações sobre todas as solicitações recebidas pelo servidor, incluindo o endereço IP do cliente, a data e hora da solicitação, o método HTTP usado, o URL solicitado, o código de status da resposta e outras informações relevantes. O arquivo de log de acesso geralmente é configurado usando a diretiva `CustomLog`.

2. **Error Log**: O arquivo de log de erro registra mensagens de erro e avisos relacionados ao servidor Apache. Isso inclui erros de configuração, erros de syntax, erros de aplicativo, falhas de autenticação, problemas de conexão, entre outros. O arquivo de log de erro é configurado usando a diretiva `ErrorLog`.

3. **LogLevel**: A diretiva `LogLevel` define o nível de detalhe dos logs de erro que são registrados. Existem várias opções disponíveis para definir o nível de log, como `emerg` (emergência), `alert` (alerta), `crit` (crítico), `error` (erro), `warn` (aviso), `notice` (aviso), `info` (informação) e `debug` (depuração). Você pode ajustar o nível de log para registrar apenas os erros mais críticos ou aumentar o nível para obter logs mais detalhados.

4. **Combined Log Format**: O formato de log combinado (`combined`) é um formato padrão amplamente usado para registros de acesso. Ele registra as informações mais comumente necessárias, como o endereço IP do cliente, a data e hora, o método HTTP, o URL solicitado, o código de status da resposta, o tamanho do arquivo enviado e o agente do usuário (user agent). Esse formato é configurado usando a diretiva `LogFormat` juntamente com a diretiva `CustomLog`.

5. **Custom Log Formats**: O Apache permite que você defina formatos personalizados para os logs de acesso, permitindo que você especifique quais informações devem ser registradas e em qual ordem. Você pode usar diferentes variáveis pré-definidas do Apache para criar um formato personalizado que atenda às suas necessidades específicas.

6. **Log Rotation**: O Apache fornece a opção de rotacionar automaticamente os arquivos de log para evitar que eles cresçam demais e ocupem muito espaço em disco. A rotação de log é feita usando utilitários como o `logrotate` no Linux. Isso permite que você mantenha um número limitado de arquivos de log e os comprima ou arquive automaticamente após um determinado período de tempo.

Essas são apenas algumas das principais opções de log disponíveis no Apache. O servidor Apache oferece uma ampla gama de recursos para registrar e monitorar as atividades do servidor, permitindo que você ajuste as configurações de log de acordo com suas necessidades específicas. Consulte a documentação oficial do Apache para obter mais informações detalhadas sobre as opções de log disponíveis.
