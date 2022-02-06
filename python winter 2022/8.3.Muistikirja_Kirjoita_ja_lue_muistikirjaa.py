"""
Luvun viimeinen tehtävä on kurssin toisen jatkuvan tehtäväsarjan ensimmäinen tehtävä. Tässä tehtävässä teemme muistikirjan, joka tallennetaan erilliseen tiedostoon nimeltä "muistio.txt".

Tee ohjelma, joka antaa käyttäjälle mahdollisuuden
(1) lukea muistikirjan sisältö,
(2) Lisätä muistikirjaan merkintä tai
(3) Tyhjentää koko muistikirja
Lisäksi lisää valinta (4), joka lopettaa ohjelman. Mikäli käyttäjä valitsee 1, tulostetaan tiedoston sisältö ruudulle, mikäli 2 niin ohjelma kysee "Kirjoita uusi merkintä: " ja tallentaa merkinnän muistioon, lisäten merkinnän loppuun rivinvaihtomerkin "\n" jotta merkinnät pysyvät eri riveillä. Jos käyttäjä valitsee 3 tyhjennetään tiedosto ja tulostetaan näytölle teksti "Muistio tyhjennetty." ja valinnalla 4 ohjelma ilmoittaa "Lopetetaan." ja sammuu. Muilla valinnoilla ohjelma ilmoittaa "Tuntematon valinta.". Toimiessaan ohjelma tulostaa seuraavaa:


(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta maitoa
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 1
-Osta maitoa

(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 4
Lopetetaan.



Huomaa, että nopein tapa tiedoston tyhjentämiseen on avata se tilaan "w" ja sulkea samantien.

"""

#Muistikirja

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

#2 Lisää merkinnän muistikirjaan
    elif kysely == 2:

        teksti = input("Kirjoita uusi merkintä: ")

        tiedosto = open("muistio.txt", "a")
        tiedosto.write(teksti)
        tiedosto.write("\n")
        tiedosto.close()

#3 Tyhjentää muistikirjan tyhjäksi

    elif kysely == 3:

        tiedosto = open("muistio.txt", "w")
        tiedosto.close()
        print ("Muistio tyhjennetty.")

#4 Lopettaa ohjelman       
    elif kysely == 4:
        print ("Lopetetaan.")
        break