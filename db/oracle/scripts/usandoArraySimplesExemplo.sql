declare 

  cursor cursor_usuarios is
   select * from usuario_v u where u.IE_SITUACAO = 'A' and rownum <= 1;
   
  a_usuarios owa.vc_arr; 
  
begin

  for r_usuarios in cursor_usuarios loop
    a_usuarios(1) := r_usuarios.nm_usuario;
    a_usuarios(2) := r_usuarios.ds_usuario;
  end loop;
  dbms_output.put_line(a_usuarios(1));
  dbms_output.put_line(a_usuarios(2));
  dbms_output.put_line('------------');
  
  
end;

-- #owa #vc_arr #owa.vc_arr #array