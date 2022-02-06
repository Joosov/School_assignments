"""
Kolmannessa tehtävässä Kilpailija-luokkaa muokataan kahdella tavalla. Ensinnäkin, kirjoita luokalle seliterivi "Kilpailija: sisältää pisteet ja värin". Toisekseen, lisää luokkaan alustusfunktio __init__, jossa uusi olio pyytää itselleen värin käyttäjän syötteenä "Anna minulle väri: ".

Pääohjelmassa tulee luoda kaksi oliota ja antaa näille alustuksessa värit "sininen" ja "punainen", tämän jälkeen kutsuen molempien tilanne-jäsenfunktiota. Lopuksi ohjelma vielä tulostaa ensimmäisen olion selostetekstin komennolla print([nimi].__doc__). Ohjelma tulostaa siis seuraavaa:

Anna minulle väri: sininen
Anna minulle väri: punainen
Olen sininen ja minulla on 0 pistettä!
Olen punainen ja minulla on 0 pistettä!
Kilpailija: sisältää pisteet ja värin


"""
class Kilpailija:
    """Kilpailija: sisältää pisteet ja värin"""
    pisteet = 0
    vari = ""

#Kysyy varin ja asettaa sen halutuksi
    def __init__(self):
        self.vari = input("Anna minulle väri: ")

#Tulostaa tilanteen
    def tilanne(self):
        print ("Olen " + self.vari + " ja minulla on " + str(self.pisteet) + " pistettä!")

#Pääohjelma ajaa Kilpailijan kaksi kertaa ja tulostaa heidän tilanteen
def main():

    henkilo1 = Kilpailija()
    henkilo2 = Kilpailija()

    henkilo1.tilanne()
    henkilo2.tilanne()

    print (Kilpailija.__doc__)

if __name__ == "__main__":
        main()