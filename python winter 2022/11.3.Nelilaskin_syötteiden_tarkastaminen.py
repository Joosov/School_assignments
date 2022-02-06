"""
Luvun kolmas tehtävä jatkaa edellisessäkin luvussa työstettyä nelilaskinta. Tähän asti ohjelma on ollut sen varassa, että käyttäjä antaa aina laskimelle oikeita lukuarvoja, mutta virheenkäsittelyn avulla tämäkin ongelma voidaan poistaa.

Tee siis ohjelmakoodiin muutokset, joilla käyttäjän antamat syötteet tarkastetaan ennen kuin ne hyväksytään laskimeen numeroiksi. Helpointa tämä on tehdä luomalla erillinen alifunktio, joka pyytää käyttäjältä niin kauan uutta lukua kunnes tyyppimuunnos kokonaisluvuksi onnistuu. Tämän jälkeen alifunktio palauttaa lukuarvon laskimelle. Jos käyttäjän syöttämä luku on virheellinen, tulostetaan "Virheellinen syöte!" ja lukua pyydetään uudestaan. Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:


Anna luku: fge
Virheellinen syöte!
Anna luku: 10
Anna luku: 15
(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut: 10 15
Tee valinta (1-8): 7
Anna luku: apina
Virheellinen syöte!
Anna luku: 20
Anna luku: 9
(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut: 20 9
Tee valinta (1-8): 8
"""
import math

def tarkistus():

#Palauttaa numeroarvon, jos luku on int
    while True:
        try:
            arvo = int(input("Anna luku: "))
            return arvo

        except ValueError:
            print ("Virheellinen syöte!")


def main():

#Ajaa alifunktion ja muuttaa arvot numeroarvoiksi

    luku1 = tarkistus()
    luku2 = tarkistus()

    while True:

#Tulostaa vaihtoehdot käyttäjälle
        print ("""(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut:""", luku1, luku2)

        valinta = int((input("Tee valinta (1-8):")))

#Jos valinta on seitsemän, kysyy uudet luvut. Muut toiminnot ovat matemaattisia
        
        if valinta == 1:
            print("Tulos on:", luku1 + luku2)

        elif valinta == 2:
            print("Tulos on:", luku1 - luku2)

        elif valinta == 3:
            print ("Tulos on:", luku1 * luku2)

        elif valinta == 4:
            print ("Tulos on:", luku1 / luku2)

        elif valinta == 5:
            print ("Tulos on:", math.sin(luku1/luku2))

        elif valinta == 6:
            print ("Tulos on:", math.cos(luku1/luku2))

        elif valinta == 7:
            luku1 = tarkistus()
            luku2 = tarkistus()

        elif valinta == 8:
            break

if __name__ == "__main__":
        main()