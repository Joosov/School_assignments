
public class Paaohjelma {

    public static void main(String[] args) {
        // Scanner lukija = new Scanner(System.in);

        
        //tekee uudet kortit
        Maksukortti pekanKortti = new Maksukortti(20);
        Maksukortti matinKortti = new Maksukortti(30);

        //Pekka ja Matti syövät maukkaasti ja edullisesti
        pekanKortti.syoMaukkaasti();
        matinKortti.syoEdullisesti();
        
        //tulostaa korttien saldon
        System.out.println("Pekka: Kortilla on rahaa " + pekanKortti + " euroa");
        System.out.println("Matti: Kortilla on rahaa" + matinKortti + " euroa");
        
        //lisää rahaa Pekan kortille
        pekanKortti.lataaRahaa(20);
        
        //Matti syö maukkaasti, vähentää Matin saldoa
        matinKortti.syoMaukkaasti();

        //tulostaa korttien saldon
        System.out.println("Pekka: Kortilla on rahaa " + pekanKortti + " euroa");
        System.out.println("Matti: Kortilla on rahaa" + matinKortti + " euroa");
        
        //Pekka syö kaksi kertaa edullisesti
        pekanKortti.syoEdullisesti();
        pekanKortti.syoEdullisesti();
        
        matinKortti.lataaRahaa(50);
        
        System.out.println("Pekka: Kortilla on rahaa " + pekanKortti + " euroa");
        System.out.println("Matti: Kortilla on rahaa" + matinKortti + " euroa");
        
        
        
        
        
        
        
       
    }
}
