/*
Bloco Script Básico
*/

declare 

  -- Declação de Variáveis
  saudacao varchar2(50);

begin
  
  saudacao := 'Jesus TE AMA!';  
  dbms_output.put_line('Olá! '||saudacao);

end;

-- #script #basico