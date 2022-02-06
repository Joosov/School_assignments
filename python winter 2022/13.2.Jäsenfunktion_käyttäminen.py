"""
Tässä tehtävässä jatketaan edellistä tehtävää. Muuta ohjelmaasi siten, että luokalla Kilpailija on kaksi jäsenfunktiota, tilanne ja maali. Kutsuttaessa funktiota tilanne olio tulostaa "Olen [vari] ja minulla on [pisteet] pistettä!". Kutsuttaessa funktiota maali olio lisää itselleen yhden pisteen.

Pääohjelma luo luokasta olion nimeltä "eka" ja antaa sille muuttujan eka.vari arvoksi "sininen". Lopuksi ohjelma kutsuu ensin jäsenfunktiota eka.maali() ja lopuksi funktiota eka.tilanne(). Ohjelma tulostaa siis seuraavaa:


Olen sininen ja minulla on 1 pistettä!

"""
#Luo luokan
class Kilpailija:
    pisteet = 0
    vari = ""
    tilanne = 0

#Luo funktiot

    def tilanne(self):
        print ("Olen " + self.vari  + " ja minulla on " + str(self.pisteet) + " pistettä!")

    def maali(self):
        self.pisteet += 1

#Pääohjelma määrittelee olion arvot
def main():

    henkilo = Kilpailija()
    henkilo.vari = "sininen"

 #Henkilö tekee maalin!   
    henkilo.maali()

#Tulostetaan henkilön tilanne kutsumalla alifunktio!
    henkilo.tilanne()

if __name__ == "__main__":
        main()