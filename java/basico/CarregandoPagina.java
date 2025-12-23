package basico;

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;

public class CarregandoPagina {

    public void getPage(URL url, File file) throws IOException {
        BufferedReader in =
                new BufferedReader(new InputStreamReader(url.openStream()));

        BufferedWriter out = new BufferedWriter(new FileWriter(file));

        String inputLine;

        while ((inputLine = in.readLine()) != null) {
		
            // Imprime página no console
            System.out.println(inputLine);
			
            // Grava pagina no arquivo
            out.write(inputLine);
            out.newLine();
        }

        in.close();
        out.flush();
        out.close();
    }

    public static void main(String[] args) {
        URL url = null;
        File file = new File("C:\\TutorialArquivos\\page.html");
        try {
            url = new URL("https://ondetrabalhar.com/vagas/1399/arquiteto-java");
            new CarregandoPagina().getPage(url, file);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}