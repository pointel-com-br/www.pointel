# quais os principais comandos  iniciados com \d no psql

No PostgreSQL (psql), o comando "\d" é usado para exibir informações sobre objetos de banco de dados, como tabelas, visualizações, índices, sequências e muito mais. Alguns dos principais comandos iniciados com "\d" no psql são:

1. \dt: Lista todas as tabelas no banco de dados atual.
2. \d [nome_da_tabela]: Mostra informações sobre uma tabela específica, incluindo colunas, tipo de dados das colunas, restrições, índices e gatilhos associados à tabela.
3. \dv: Lista todas as visualizações no banco de dados atual.
4. \di: Lista todos os índices no banco de dados atual.
5. \ds: Lista todas as sequências no banco de dados atual.
6. \df: Lista todas as funções (procedimentos armazenados) no banco de dados atual.
7. \dn: Lista todos os esquemas (schemas) no banco de dados atual.
8. \du: Lista todos os usuários/roles no banco de dados.

Esses são apenas alguns exemplos dos comandos iniciados com "\d" no psql. Você pode usar "\d" seguido de outros objetos de banco de dados, como "\dp" para listar permissões, "\dc" para listar classes de conexão e assim por diante.

Lembrando que esses comandos fornecem informações sobre os objetos de banco de dados, mas não realizam ações de modificação. Para executar ações como inserir, atualizar ou excluir dados, você precisa usar comandos SQL regulares.
