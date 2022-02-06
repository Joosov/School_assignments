"""
Tässä tehtävässä jatketaan luvun 4 neljättä tehtävää, laskinta. Tehtävässä lisätään laskimeen kaksi uutta tehtävää, sin ja cos. Nämä funktiot löytyvät math-moduulin sisältä, vastaavilla funktionimillä sin() ja cos(), joille molemmille voidaan antaa syötteeksi (luku_1 / luku_2). Toteuta käskyt vaihtoehdoiksi 5 ja 6, samalla siirtäen "vaihda luvut" ja "Lopeta" kohdiksi 7 ja 8. Ohjelma toimii seuraavalla tavalla:


Anna ensimmäinen luku: 1
Anna toinen luku: 2
(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut: 1 2
Tee valinta (1-8): 5
Tulos on: 0.479425538604
(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut: 1 2
Tee valinta (1-8): 6
Tulos on: 0.87758256189
(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut: 1 2
Tee valinta (1-8): 8
"""

# -*- coding: cp1252 -*-

import math

#Kysyy ensimmäisen ja toisen luvun
luku1 = int(input("Anna ensimmäinen luku:" ))
luku2 = int(input("Anna toinen luku: "))

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

##Jos valinta on seitsemän, kysyy uudet luvut. Muut toiminnot ovat matemaattisia
    
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
        luku1 = int(input("Anna uusi ensimmäinen luku:" ))
        luku2 = int(input("Anna uusi toinen luku: "))

    elif valinta == 8:
        break