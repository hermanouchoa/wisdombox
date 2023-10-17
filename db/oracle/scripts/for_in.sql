-- Script abaixo faz uso de FOR .. IN 
declare 
  -- Variaveis Locais
  nr_seq NUMBER(10);
begin
  dbms_output.put_line('Iniciando Execução do Script...');
    for reg in (
      --Aplicando um Select qualquer para obter os dados do loop
      select s.cd_setor_atendimento, s.cd_estabelecimento 
      from setor_atendimento_v s
      where s.cd_estabelecimento = 4 and s.ie_situacao = 'A'
      ) loop

          --Select abaixo eu utilizo para obter o próximo número de uma sequence
          select QUA_REGRA_SETOR_VINC_SEQ.NEXTVAL new_seq 
              into nr_seq
              from dual;

          -- Exibindo algo no output...
          dbms_output.put_line(reg.cd_setor_atendimento||';'||reg.cd_estabelecimento||';'||nr_seq||';');

          --Realizando uma operação de insert com base nos dados do loop
          insert into QUA_REGRA_SETOR_VINC
          (
              nr_sequencia,
              cd_estabelecimento,
              cd_setor_atendimento,
              dt_atualizacao,
              nm_usuario,
              dt_atualizacao_nrec,
              nm_usuario_nrec,
              ie_situacao
          )
          values
          (
          nr_seq,
          reg.cd_estabelecimento,
          reg.cd_setor_atendimento,
          sysdate,
          'tasy',
          sysdate,
          'tasy',
          'A'
          ); 
          commit;
      
      end loop;
  dbms_output.put_line('Finalizando Execução do Script...');
end;