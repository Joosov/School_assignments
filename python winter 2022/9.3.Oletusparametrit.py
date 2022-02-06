"""
Luvun kolmas tehtävä muokkaa eteenpäin luvun ensimmäistä tehtävää. Tällä kertaa tulostaja-funktion toimintaa muutetaan siten, että se vastaanottaa yhden parametrin, jonka oletusarvona on "Oletustulostus" ja tulostaa saamansa arvon.

Pääfunktio taas pyytää käyttäjältä syötettä "Anna syöte (Lopeta lopettaa): ", ja mikäli käyttäjä antaa syötteen, joka on 5 tai useampi merkkiä, lähetetään se tulostaja-alifunktiolle. Muussa tapauksessa alifunktiota kutsutaan ilman parametriä. Jos käyttäjä antaa syötteen "Lopeta", ohjelma sammuu. Ohjelma toimii seuraavalla tavalla:


Anna syöte (Lopeta lopettaa): Pitkäsana
Pitkäsana
Anna syöte (Lopeta lopettaa): möh
Oletustulostus
Anna syöte (Lopeta lopettaa): Toinenkovinpitkäsana
Toinenkovinpitkäsana
Anna syöte (Lopeta lopettaa): Lopeta



Merkkijonon pituuden mittaaminen onnistuu helpoiten komennolla len().
"""

jatkuu = True

def tulostaja(sana):

#Jos sana on alle viisi merkkiä, tulostaa oletustulostuksen
    if (len(sana)<5):
        print ("Oletustulostus")
    else:
        print (sana)

def main():

 #Jos input ei ole Lopeta, kutsuu alifunktion 

    while True:

        tulostus = input("Anna syöte (Lopeta lopettaa):")
        if tulostus != ("Lopeta"):
            tulostaja(tulostus)
            
        else:
            break

if __name__ == "__main__":
    main()