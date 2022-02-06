"""
Kolmas esimerkki on ensimmäinen tehtävä, jossa luodaan käyttäjälle valikko. Käyttäjältä pyydetään luku väliltä 1-3, ja sen mukaan, mitä käyttäjä valitsee tulostetaan joko "Haukion kala Oy" valinnalla 1, "Metallipaja VasaraAika" valinnalla 2 tai "Balin palapelitehdas" valinnalla 3. Toimiessaan ohjelma tulostaa esimerkiksi seuraavaa:


Valitse kohde (1-3): 1
Haukion kala Oy



Example output:
Valitse kohde (1-3): 3
Balin palapelitehdas
"""

yhtio1 = "Haukionkala Oy"
yhtio2 = "Metallipaja VasaraAika"
yhtio3= "Balin palapelitehdas"

luku = int(input("Valitse kohde (1-3): "))

if luku == 1:
    print(yhtio1)
    
elif luku == 2:
    print (yhtio2)

elif luku == 3:
    print (yhtio3)