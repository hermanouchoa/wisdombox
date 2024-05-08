package basico;
import java.util.ArrayList;

/**
 *
 * @author Hermano Uchoa - https://github.com/hermanouchoa
 */
public class ArrayList_Declaracao {
    /**
     * 
     * @param args 
     */
    public static void main(String[] args) {
        
        ArrayList<String> nomes = new ArrayList<>();
        nomes.add("Jesus");
        nomes.add("Maria");
        nomes.add("José");
        
        System.out.println("\nLista de Nomes:");
        for (String nome : nomes) {
            System.out.println(nome);
        }
        
    }    
}