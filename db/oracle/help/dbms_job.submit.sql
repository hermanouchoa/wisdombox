/*
Utilizo esses blocos de comandos para criação de JOBs no Oracle
*/

-- Criação de um JOB utilizando DBMS_JOB
declare
    variable jobno number;
begin
    dbms_job.submit(:jobno
                   ,'PROCEDURE_QUE_SERA_EXECUTADA_PELA_JOB(PARAMETRO1, PARAMETRO2)'
                   ,sysdate
                   ,'TRUNC(SYSDATE + 1) + 01/24'
                   );
end;

/

-- Criação de um JOB utilizando DBMS_SCHEDULER
BEGIN  
    DBMS_SCHEDULER.CREATE_JOB (
        job_name        => 'NOME_DA_SUA_JOB',
        job_type        => 'PLSQL_BLOCK',
        job_action      => 'BEGIN PROCEDURE_QUE_SERA_EXECUTADA_PELA_JOB(PARAMETRO1, PARAMETRO2); END;',
        start_date      => SYSTIMESTAMP, --TRUNC(SYSTIMESTAMP + INTERVAL ''1'' DAY) + INTERVAL ''4'' HOUR,
        repeat_interval => 'FREQ=DAILY; BYHOUR=8; BYMINUTE=30; BYSECOND=0',
        enabled         => TRUE,
        auto_drop       => FALSE,
        comments        => 'JOB diário para executar rotina de coleta de dados para BI financeiro, às 8:30.'
    );
END;
/

-- Selecionar informações do JOB criado
SELECT job_name, state, last_start_date, next_run_date
FROM dba_scheduler_jobs
WHERE job_name = 'NOME_DA_SUA_JOB';



/*
    # job, dbms_job.submit, dbms_job, DBMS_SCHEDULER
*/