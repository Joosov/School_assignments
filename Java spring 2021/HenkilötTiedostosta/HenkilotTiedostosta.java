
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class HenkilotTiedostosta {

    public static void main(String[] args) {
        Scanner lukija = new Scanner(System.in);

        System.out.println("Minkä niminen tiedosto luetaan?");
        String tiedosto = lukija.nextLine();

        ArrayList<Henkilo> henkilot = lueHenkilot(tiedosto);
        System.out.println("Henkilöitä: " + henkilot.size());
        System.out.println("Henkilöt:");
        for (Henkilo henkilo : henkilot) {
            System.out.println(henkilo);

        }
    }

    public static ArrayList<Henkilo> lueHenkilot(String tiedosto) {
        ArrayList<Henkilo> henkilot = new ArrayList<>();

        // toteuta henkilöiden lukeminen ja luominen tänne
        
        //lukee tiedoston läpi
        try (Scanner skanneri = new Scanner(Paths.get(tiedosto))) {
            while (skanneri.hasNextLine()) {
                //tallentaa skannerin luetun rivin
                String rivi = skanneri.nextLine();
                
                //jakaa splitin avulla palat stringiin
                String[] palat = rivi.split(",");
                
                
                String nimi = palat[0];
                int ika = Integer.valueOf(palat[1]);
                
                //lisää iän ja nimen henkilö arraylistiin
                henkilot.add(new Henkilo(nimi, ika));
            }
        } catch (IOException ex) {
            Logger.getLogger(HenkilotTiedostosta.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        return henkilot;

        
    }
}
