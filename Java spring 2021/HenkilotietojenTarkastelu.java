
import java.util.ArrayList;
import java.util.Scanner;

public class HenkilotietojenTarkastelu {

    public static void main(String[] args) {
        Scanner lukija = new Scanner(System.in);

        //tallennus
        int summa = 0;
        int lukumaara = 0;
        int apua = 0;
        int pisinnimi;
        String apuri = "";

        while (true) {
            String luettu = lukija.nextLine();
            if (luettu.equals("")) {
                break;
            }

            String[] palat = luettu.split(",");
            //lisää summan
            summa = summa + Integer.valueOf(palat[1]);
            //lisää lukumäärän
            lukumaara = lukumaara + 1;
            //pisin nimi = palat[0] pituus!
            pisinnimi = palat[0].length();

            /*jos int apua on pienempi kuin  int pisin nimi, apua on pisin nimi. 
            Ja String apuri on tällöin palat[0]!*/
            if (apua < pisinnimi) {
                apua = pisinnimi;
                apuri = palat[0];

            }
        }
        //tulostukset
        System.out.println("Pisin nimi: " + apuri);
        System.out.println("Syntymävuosien keskiarvo:" + (1.0 * summa / lukumaara));
    }
}
