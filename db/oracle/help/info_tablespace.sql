-- Utilizo o SQL abaixo para obter informações sobre espaço no data files, por tablespace
SELECT df.tablespace_name "Tablespace",
  totalusedspace "Used MB",
  (df.totalspace - tu.totalusedspace) "Free MB",
  df.totalspace "Total MB",
  ROUND(100 * ( (df.totalspace - tu.totalusedspace)/ df.totalspace)) "% Free", autoextensible
FROM
  (SELECT tablespace_name,
    ROUND(SUM(bytes) / 1048576) TotalSpace, AUTOEXTENSIBLE autoextensible
  FROM dba_data_files
  GROUP BY tablespace_name, AUTOEXTENSIBLE
  ) df,
  (SELECT ROUND(SUM(bytes)/(1024*1024)) totalusedspace,
    tablespace_name
  FROM dba_segments
  GROUP BY tablespace_name
  ) tu
WHERE df.tablespace_name = tu.tablespace_name;
 
 -- #datafile, tablespace