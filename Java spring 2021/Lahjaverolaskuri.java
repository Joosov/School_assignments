
import java.util.Scanner;

public class Lahjaverolaskuri {

    public static void main(String[] args) {
        Scanner lukija = new Scanner(System.in);
        
        System.out.println("Lahjan suuruus?");
        double lahja = Integer.valueOf(lukija.nextLine());  
        
        double vero1 = (100 + (lahja - 5000) *0.08);
        double vero2 = (1700 + (lahja - 25000) *0.10 );
        double vero3 = (4700 + (lahja - 55000 )*0.12);
        double vero4 = (22100 + (lahja - 200000 )*0.15);
        double vero5 = (142100 + (lahja - 1000000 )*0.17);

        if (lahja < 5000 ) {
            System.out.println("Ei veroa!");
           
        }   else if (lahja <= 25000) {
            System.out.println("Vero: " + vero1);  
            
        }   else if (lahja <= 55000) {
            System.out.println("Vero: " + vero2);
            
        }   else if (lahja <= 200000 ) {
            System.out.println("Vero " + vero3);
            
        }   else if (lahja <= 1000000 ) {
            System.out.println("Vero " + vero4);
            
        }   else if (lahja >= 1000000 ) {
            System.out.println("Vero " + vero5);
            
        }
    }
}
