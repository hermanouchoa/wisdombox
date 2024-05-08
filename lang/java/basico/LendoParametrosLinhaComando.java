package basico;

import java.util.Arrays;

public class LendoParametrosLinhaComando {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(args));

        if ( args.length <= 1 ) {
            System.out.println("Use: java LendoParametrosLinhaComando [pt|en] [seu nome]");
        } else if(args[0].equals("en")){
            System.out.printf("Hello, %s!%n", args[1]);
        } else if(args[0].equals("pt")){
            System.out.printf("Ola, %s!%n", args[1]);
        }
    }
}

/*
 * Exemplo> de como usar a Classe pelo prompt
 *      java LendoParametrosLinhaComando.java en Hermano
 *      java LendoParametrosLinhaComando.java pt Joao
 */
