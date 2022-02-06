"""
Neljäs tehtävä lisää ohjelmaan paluuarvon. Tee ohjelma, jossa on pääfunktio main ja alifunktio pituusmitta. pituusmitta saa syötteenä parametrin ja mittaa tämän parametrin pituuden, palauttaen sen integer-arvona pääohjelmalle.

Pääohjelma pyytää käyttäjältä syötettä "Anna syote (Lopeta lopettaa): " ja lähettää syötteen mitattavaksi. Jos tulos on 0, ohjelma vastaa "Et antanut syötettä", muuten "Antamasi syöte oli [pituus] merkkiä pitkä.". Jos käyttäjä antaa arvon Lopeta, ohjelma sammuu. Ohjelma tulostaa seuraavaa:


Anna syöte (Lopeta lopettaa): sihijuomaa
Antamasi syöte oli 10 merkkiä pitkä.
Anna syöte (Lopeta lopettaa): nahkasaapasharja
Antamasi syöte oli 16 merkkiä pitkä.
Anna syöte (Lopeta lopettaa): 
Et antanut syötettä
Anna syöte (Lopeta lopettaa): Lopeta


"""

def pituusmitta(luku):

#Laskee luvun pituuden 
    luku = int(len(luku))

#Jos luvun pituus on pidempi kuin 0, tulostaa merkkirivistön pituuden
    if (luku > 0):
        print ("Antamasi syöte oli", luku, "merkkiä pitkä.")
        return luku

#Jos ei ole, palauttaa seuraavan tulostuksen
    else:
        print ("Et antanut syötettä")

def main():

    while True:

#Kysyy syötettä, jos syöte on Lopeta, lopettaa, muuten ajaa aliohjelman
        syote = input("Anna syöte (Lopeta lopettaa): ")
        if syote == ("Lopeta"):
            break
        else:
            pituusmitta(syote)

if __name__ == "__main__":
    main()