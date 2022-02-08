
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class Urheilutilastot {

    public static void main(String[] args) {
        Scanner lukija = new Scanner(System.in);

        int apuri = 0;
        int homewins = 0;
        int tappiot = 0;
        

        System.out.println("Minkä niminen tiedosto luetaan? ");
        String tiedosto = lukija.nextLine();

        //luo uuden listan
        //ArrayList<String> lista = new ArrayList<>();
        System.out.println("Minkä nimisen joukkueen tiedot tulostetaan? ");
        //tallentaa kyselyksi halutun joukkueen
        String kysely = lukija.nextLine();

        //käy läpi String tiedoston
        try (Scanner skanneri = new Scanner(Paths.get(tiedosto))) {

            //lisää riviin skannatut tiedostot
            while (skanneri.hasNextLine()) {
                String rivi = skanneri.nextLine();

                //jakaa rivin osat palasiin, pilkku jakaa
                String[] palat = rivi.split(",");

                //palat 0 ja 1 kuuluvat joukkueeseen
                String koti = palat[0];
                String joukkue = palat[1];
                String kotipisteet = palat[2];
                String vieraspisteet = palat[3];
                
                int kotivoitot = Integer.valueOf(palat[2]);
                int vierasvoitot = Integer.valueOf(palat[3]); 

//jos koti tai joukkue stringissä on kyselty termi, lisätään se apuriin sekä
//voittoihin ja tappioihin
                if (koti.contains(kysely) || (joukkue.contains(kysely))) {
                    apuri++;
 
                }
                //tässä rumaa koodia
                //jos kotipisteet on suuremmat kuin vieraan pisteet, voitot kasvaa
                if (kotivoitot > vierasvoitot && koti.contains(kysely)) {
                    homewins++;
                    
                //jos kysytty joukkue pelaa vieraana ja voittaa, kasvattaa se myös voittoja
                } if (kotivoitot < vierasvoitot && joukkue.contains(kysely)) {
                    homewins++;
                }
                //jos kotijoukkeen pisteet on pienempi kuin vieraan
                if (kotivoitot < vierasvoitot && koti.contains(kysely)) {
                    tappiot++;
                }
                
                if (kotivoitot > vierasvoitot && joukkue.contains(kysely)) {
                    tappiot++;
                }
            }
            //virheilmoitus, jos olemassa olevaa tiedostoa ei löydy
        } catch (IOException ex) {
            //Logger.getLogger(LoytyykoTiedostosta.class.getName()).log(Level.SEVERE, null, ex);
            System.out.println("Tiedoston " + tiedosto + " lukeminen epäonnistui");
        }
        //tulostaa apurin
        System.out.println("Otteluita: " + apuri);
        System.out.println("Voittoja: " + homewins);
        System.out.println("Tappioita: " + tappiot);
    }
}
