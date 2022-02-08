
import java.util.Scanner;

public class VanhimmanNimi {

    public static void main(String[] args) {
        Scanner lukija = new Scanner(System.in);

        int vanhin = 0;
        String asd = "";
                
        while (true) {
            String luettu = lukija.nextLine();
            if (luettu.equals("")) {
                break;
            }
            String[] palat = luettu.split(",");

            if (Integer.valueOf(palat[1]) > vanhin) {
                vanhin = Integer.valueOf(palat[1]);
                asd = palat[0];
                
            } }
             System.out.println("Vanhimman nimi: " + asd);
        }

    }
