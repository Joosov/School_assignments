"""
Luvun viimeinen tehtävä liittyy muistikirjan käsittelyyn. Tällä kertaa ohjelmaa muutetaan siten, että ohjelma lisää muistikirjamerkinnän perään päiväyksen ja kellonajan, josta käy ilmi milloin merkintä on tehty.Lisäksi laita viestin ja päiväyksen väliin eroitin ":::" (kolme kaksoispistettä).

Päiväys saadaan esimerkiksi time-moduulista komennolla


	
>>> import time		
>>> time.strftime("%X %x")
'19:01:34 01/03/09'
>>> 



joka palauttaa kellonajan ja päiväyksen merkkijonona. Kun tämä merkkijono liitetään viestiin, saadaan ohjelma toimimaan muodossa:


(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Soita Ekille
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 1
-Soita Ekille:::19:06:39 01/03/09

(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 4
Lopetetaan.


"""

# -*- coding: cp1252 -*-

#Muistikirja

import time

while True:

#Muistikirjan vaihtoehdot ja kysely

    print("""(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
""")

    kysely = int(input("Mitä haluat tehdä?: "))


#1 Tulostaa kirjoitetut tiedot
    if kysely == 1:
        tiedosto = open("muistio.txt", "r")
        print (tiedosto.read())

        tiedosto.close()

#2 Lisää merkinnän muistikirjaan ja aikaleiman
    elif kysely == 2:

        teksti = input("Kirjoita uusi merkintä: ")

        tiedosto = open("muistio.txt", "a", )
        tiedosto.write(teksti)
        tiedosto.write(":::")
        tiedosto.write(time.strftime("%X %x"))
        tiedosto.write("\n")
        tiedosto.close()

#3 Tyhjentää muistikirjan tyhjäksi

    elif kysely == 3:

        tiedosto = open("muistio.txt", "w")
        tiedosto.close()
        print ("Muistio tyhjennetty.")

#4 Lopettaa ohjelman       
    if kysely == 4:
        print ("Lopetetaan.")
        break