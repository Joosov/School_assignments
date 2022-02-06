"""
Toinen 4. luvun ohjelmointitehtävä liittyy avoimeen toistoon, jossa toistorakenne toteutetaan siten, että käyttäjän syötteet ratkaisevat sen milloin ohjelma lopetetaan.

Toteuta ohjelma, joka joka kierroksen alussa pyytää käyttäjältä merkkijonon ja tulostaa sen ruudulle. Ainoan poikkeuksen tähän tekee tilanne, jossa käyttäjä kirjoittaa tekstin "lopeta", jolloin ohjelma tulostaa tekstin "Lopetit ohjelman" ja sammuu. Toimiessaan oikein ohjelma tulostaa seuraavaa:


Kirjoita jotain: testi
testi
Kirjoita jotain: Urjala
Urjala
Kirjoita jotain: lopeta
Lopetit ohjelman.



Ohjelma kannattaa sijoittaa yhden "while True:"-rakenteen sisään, ja katkaisuehto sitoa if-valintarakenteeseen ja break-käskyyn.
"""

jatkuu = True

while True:
    teksti = input("Kirjoita jotain: ")

    if teksti == "lopeta":
        jatkuu = False
        print ("Lopetit ohjelman.")
        break
    
    else: 
        print (teksti)
