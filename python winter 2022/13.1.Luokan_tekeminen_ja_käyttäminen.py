"""
Luvun 10 tehtävissä ei enää koodata varsinaisesti toiminnallisia ohjelmia, vaan kokeillaan erilaisten esimerkkikoodien avulla luokkamäärittelyn tekemistä ja olioiden perustoimintoja. Tämä sen vuoksi, että kurssi ei varsinaisesti keskity olio-ohjelmointiin, vaan pyrkii ainoastaan ohjaamaan siinä alkuun ja ymmärtämään miten se eroaa proseduraalisesta ohjelmoinnista.

Ensimmäisessä oliotehtävässä luodaan määritellään luokkaa nimeltä Kilpailija, jolle annettaan kaksi jäsenmuuttujaa, pisteet ja vari. Tämän jälkeen luo luokasta olio "eka", jolle annetaan muuttujan vari arvoksi sininen ja pisteet arvoksi 10. Lopuksi laita ohjelmasi vielä tulostamaan olion tiedot muodossa "Kilpailijalla [väri] on [pisteet] pistettä!", eli näin:


Kilpailijalla sininen on 10 pistettä!

"""
#Luo luokan
class Kilpailija:
    pisteet = ""
    vari = ""

#Luo olion
    def eka(self):
        print ("Kilpailijalla " + self.vari + " on " + self.pisteet + " pistettä!")

#Pääohjelma määrittelee olion tiedot
def main():
    henkilo = Kilpailija()
    henkilo.vari = "sininen"
    henkilo.pisteet = "10"
    henkilo.eka()

if __name__ == "__main__":
        main()