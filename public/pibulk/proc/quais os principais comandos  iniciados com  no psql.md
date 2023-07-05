# quais os principais comandos  iniciados com \ no psql

No PostgreSQL (psql), o caractere "\" é usado como um caractere de escape para executar comandos especiais. Alguns dos principais comandos iniciados com "\" no psql são:

1. \l: Lista todos os bancos de dados disponíveis.
2. \c [nome_do_banco_de_dados]: Conecta-se a um banco de dados específico.
3. \dt: Lista todas as tabelas no banco de dados atual.
4. \d [nome_da_tabela]: Mostra informações sobre uma tabela específica.
5. \du: Lista todos os usuários/roles no banco de dados.
6. \q: Sai do psql.
7. \h [comando]: Mostra ajuda sobre um comando específico.
8. \e: Abre um editor para escrever uma consulta SQL.
9. \i [caminho_do_arquivo]: Executa um arquivo SQL.
10. \timing [on/off]: Ativa ou desativa o relatório de tempo de execução.

Esses são apenas alguns exemplos dos comandos especiais disponíveis no psql. Você pode usar "\?" para obter uma lista completa de todos os comandos disponíveis no psql e obter mais informações sobre cada comando usando "\h [comando]".

Lembrando que o caractere "\" é usado como escape apenas no psql, e não em consultas SQL regulares. Em consultas SQL regulares, não há necessidade de usar o "\" como caractere de escape.
