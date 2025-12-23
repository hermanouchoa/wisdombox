/* Script para liberar todas as funções de schema para um usuário,
   caso ele ainda não possua acesso a elas. */

/* Ative a saída antes de rodar */
SET SERVEROUTPUT ON SIZE UNLIMITED;

DECLARE
    v_sql     VARCHAR2(4000);
    v_count   PLS_INTEGER := 0;               -- Quantos GRANTs já foram executados
    v_step    CONSTANT PLS_INTEGER := 10000;  -- Intervalo de progresso
    v_usuario CONSTANT VARCHAR2(30) := 'usuario_exemplo'; -- Substitua pelo usuário desejado, que vai receber os privilégios
    v_usuario_upper CONSTANT VARCHAR2(30) := UPPER('usuario_owner'); -- Substitua pelo usuário dono dos objetos
BEGIN
    FOR r IN (
        SELECT owner,
               object_name
          FROM all_objects
         WHERE object_type = 'FUNCTION' --Ajuste para usar com outros tipos, se necessário
           AND owner        = 'TASY'
           AND object_name NOT IN (
                 SELECT table_name
                   FROM dba_tab_privs
                  WHERE grantee = UPPER(v_usuario)
                    AND type    = 'FUNCTION'
                    AND upper(owner)   = v_usuario_upper --Usuario que possui os privilégios, Owner dos objetos
             )
    )
    LOOP
        v_sql := 'GRANT EXECUTE ON ' ||
                 r.owner || '.' || r.object_name ||
                 ' TO ' || v_usuario;

        EXECUTE IMMEDIATE v_sql;
        v_count := v_count + 1;

        /* Exibe progresso a cada 10 000 registros */
        IF MOD(v_count, v_step) = 0 THEN
            DBMS_OUTPUT.PUT_LINE(v_count || ' objetos liberadas até agora…');
        END IF;
    END LOOP;

    /* Resumo final */
    DBMS_OUTPUT.PUT_LINE('Total de objetos liberadas: ' || v_count);
END;
/
