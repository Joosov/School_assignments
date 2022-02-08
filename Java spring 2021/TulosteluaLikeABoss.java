
public class TulosteluaLikeABoss {

    public static void tulostaTahtia(int maara) {
        // tehtävän ensimmäinen osa
        
        //Tallentaa numeron, joka kasvaa ohjelman myötä.
        
        int laskuri= 0;
        
        //Kun maara on pienempi kuin laskuri, ohjelma tulostaa yhden tähden.
        //Kun määrä kasvaa, kasvavat myös tulostettavat tähdet.
        while (laskuri < maara) {
            System.out.print("*");
            laskuri++;  
        } 
        System.out.println("");
    }

    public static void tulostaTyhjaa(int maara) {
        // tehtävän osa 1
        
        int tyhja = 0;
        
        while (tyhja < maara) {
            System.out.print(" ");
            tyhja++;
        }
    }

    public static void tulostaKolmio(int koko) {
        // tehtävän osa 2
        
        int tahtienmaara = 1;
        
        
        /*tähtien määrä lähtee yhdestä. Kun koko on esim 5, ohjelma
        tulostaa tyhjää 5 - 1 ja tähtiä int-muuttujassa esitetyn määrän.
        Tähtien määrä myös kasvaa, mikä kutistaa tyhjän tulostusta.*/
        
        while (tahtienmaara <= koko) {
            tulostaTyhjaa(koko - tahtienmaara);
            tulostaTahtia(tahtienmaara);
            tahtienmaara++;
        }

    }

    public static void jouluKuusi(int korkeus) {
        // tehtävän osa 3
        
        int tahtienmaara = 1;
        int jalka = 0;

        /*laskuri noudattaa samaa kaavaa kuin tulostaKolmio. Tähtien määrän
        pitää kuitenkin kasvaa enemmän kuin tyhjien määrän.
        */
        
        while (tahtienmaara <= korkeus) {
            tulostaTyhjaa(korkeus - tahtienmaara);
            tulostaTahtia((tahtienmaara * 2)-1);
            tahtienmaara= tahtienmaara + 1; 
        }
            
        while (jalka < 2) {
            tulostaTyhjaa(korkeus -2);
            tulostaTahtia(3);
            jalka= jalka + 1;
        }
        
    }

    public static void main(String[] args) {
        // Testit eivät katso main-metodia, voit muutella tätä vapaasti.

        tulostaKolmio(5);
        System.out.println("---");
        jouluKuusi(4);
        System.out.println("---");
        jouluKuusi(10);
    }
}
