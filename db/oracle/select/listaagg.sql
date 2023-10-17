-- SEM LISTAGG
select 
    cddd_fonp, cfonefonp
from   hssfonp 
where  nnumepess = 123; 

/*

Em um select comum, como o acima, o resultado será assim:

-------------------------------------------
cddd_fonp    | cfonefonp
-------------------------------------------
85           | 123456789  
85           | 987456321
-------------------------------------------
*/

-- #############################################################

-- COM LISTAGG
select 
    LISTAGG('(' || cddd_fonp || ')' || cfonefonp, '/') WITHIN GROUP (ORDER BY 1) as telefones
from   hssfonp 
where  nnumepess = 123; 

/*

Usando a função do Oracle LISTAGG vamos ter um valor único como resultado, agrupando todos os valores consultados em apenas uma linha.

-------------------------------------------
telefones
-------------------------------------------
(85)123456789/(85)987456321
-------------------------------------------

*/