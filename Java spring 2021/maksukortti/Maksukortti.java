/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Lenovo
 */
public class Maksukortti {

    private double saldo;

    public Maksukortti(double alkusaldo) {

        this.saldo = alkusaldo;
    }

    public String toString() {

        //palauttaa Stringin
        return "Kortilla on rahaa " + this.saldo + " euroa";
    }

    public void syoEdullisesti() {
        
        //vähentää edullisen määrän saldosta, kunhan se ei mene negatiiviseksi
        if (this.saldo >= 2.60) {
            this.saldo = this.saldo - 2.60;
        }

    }

    //vähentää maukkaan määrän saldosta, kunhan se ei mene negatiiviseksi
    public void syoMaukkaasti() {

        if (this.saldo >= 4.60) {
            this.saldo -= 4.60;
        }
    }
    
    public void lataaRahaa(double rahamaara) {
        
        //lisää rahamäärän, kunhan se ei ole negatiivinen
        if (rahamaara > 0) {
            this.saldo = this.saldo + rahamaara;
        }
        
        //jos saldo meinaa nousta suuremmaksi kuin 150, näyttää se saldon 150
        if (this.saldo > 150) {
        this.saldo = 150; }
    }
}
