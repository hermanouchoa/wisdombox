/*
Para saber quantas tabelas existem em um banco Oracle 19c, há várias formas — dependendo se você quer contar apenas as suas tabelas, as de todos os usuários, ou de um schema específico.
Segue um resumo com exemplos:
*/

---
-- 1. Contar as tabelas do seu usuário (schema atual)
SELECT COUNT(*) AS qtd_tabelas
FROM user_tables;
-- Retorna o número de tabelas criadas pelo usuário logado.

---
-- 2. Contar as tabelas de um schema específico
SELECT COUNT(*) AS qtd_tabelas
FROM all_tables
WHERE owner = 'NOME_DO_SCHEMA';
-- > Substitua `NOME_DO_SCHEMA` pelo nome do schema (em maiúsculas).

---
-- 3. Contar todas as tabelas existentes no banco
SELECT COUNT(*) AS qtd_tabelas
FROM dba_tables;
-- > Requer privilégios de administrador (`SELECT_CATALOG_ROLE` ou `DBA`).

---
-- 4. Listar e contar ao mesmo tempo
-- Se quiser ver os nomes e conferir manualmente:
SELECT table_name
FROM user_tables
ORDER BY table_name;

--Ou com contagem e agrupamento por schema:
SELECT owner, COUNT(*) AS qtd_tabelas
FROM all_tables
GROUP BY owner
ORDER BY qtd_tabelas DESC;


---
-- Exemplo de saída
/*
| OWNER  | QTD_TABELAS |
| ------ | ----------- |
| HR     | 32          |
| SCOTT  | 14          |
| SYSTEM | 512         |
*/
