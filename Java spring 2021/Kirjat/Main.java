
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // toteuta tänne toiminnallisuus, jonka avulla käyttäjä voi syöttää
        // kirjoja sekä tarkastella niitä

        ArrayList<Kirja> kirjat = new ArrayList<>();
        Scanner lukija = new Scanner(System.in);

        while (true) {

            //kysytään halutut tiedot
            System.out.println("Nimi: ");
            String nimi = lukija.nextLine();

            //lopettaa, jos kirjan nimi on tyhjä
            if (nimi.isEmpty()) {
                break;
            }

            //jatkaa kyselyä
            System.out.print("Sivuja: ");
            int sivuja = Integer.valueOf(lukija.nextLine());

            System.out.print("Julkaisuvuosi: ");
            int julkaisuvuosi = Integer.valueOf(lukija.nextLine());

            //tallentaa annetut tiedot arraylistiin
            kirjat.add(new Kirja(nimi, sivuja, julkaisuvuosi));
        }

        System.out.print("Mitä tulostetaan? ");
        String pyynto = lukija.nextLine();

            //jos pyyntö on "kaikki"
            if ("kaikki".equals(pyynto)) {
                //tulostaa kaiken!
                System.out.println(kirjat);
            }
            
            //jos pyyntö on nimi, käy läpi listan ja tulostaa nimet
            if ("nimi".equals(pyynto)) {
                for (Kirja kirja : kirjat) {
                    System.out.println(kirja.getNimi());
                }
            }
        }
    }
