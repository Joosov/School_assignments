"""
Myös muistikirja on tähän asti toiminut sen varassa, että käyttäjä ei yritä lukea muistiota ennen kuin tiedostoon on kirjoitettu jotain. Tällä kertaa muistikirja-ohjelmaan lisätäänkin kaksi uutta toimintoa; ensinnäkin ohjelman tulee tarkastaa käynnistyessään onko tiedosto "muistio.txt" olemassa, ja tarvittaessa luoda tämänniminen tiedosto. Mikäli näin tehdään ilmoittaa ohjelma "Oletusmuistiota ei löydy, luodaan tiedosto".

Toisekseen, lisää ohjelmaan mahdollisuus vaihtaa muistiotiedostoa kesken ohjelman suorituksen lisäämällä ohjelmaan valinta "(4) Vaihda muistiota", jonka jälkeen ohjelma pyytää uutta muistiotiedostoa "Anna tiedoston nimi: " ja tarvittaessa luo tämännimisen tiedoston jälleen antaen ilmoituksen "Tiedostoa ei löydy, luodaan tiedosto.". Lisäksi ohjelma kertoo päävalikossa mitä tiedostoa tällähetkellä käytetään; "Käytetään muistiota: [tiedostonnimi]". Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:


Oletusmuistioa ei löydy, luodaan tiedosto.
Käytetään muistiota:  muistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta maitoa
Käytetään muistiota:  muistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 4
Anna tiedoston nimi: uusimuistio.txt
Tiedostoa ei löydy, luodaan tiedosto.
Käytetään muistiota:  uusimuistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta ananas
Käytetään muistiota:  uusimuistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 1
-Osta ananas:::13:53:00 01/04/09

Käytetään muistiota:  uusimuistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 5
Lopetetaan.



Ohjelman toteuttamisessa kannattaa lähestyä ongelmaa siten, että käytettävän tiedoston nimi on tallennettuna muuttujaan, jonka arvoa muutetaan jos tiedostoa vaihdetaan. Lisäksi tiedoston olemassaolon tarkastun on helpointa toteuttaa yrittämällä avata tiedosto ja sulkemalla se samantien; jos ohjelma palauttaa IOErrorin voidaan samanniminen tiedosto luoda kirjoitustilalla.
"""
#Muistikirja

import time

def uusi():

    try:
        open("muistio.txt","r")

#Jos virhettä ei löydy, ajetaan exception ja luodaan tiedosto muistio.txt
    except Exception:
        print ("Oletusmuistioa ei löydy, luodaan tiedosto.")
        open("muistio.txt", "w")

def main():

#määrittelee käytetyn tiedoston nimen
    muistio = "muistio.txt"

#Kutsuu alifunktion uusi()
    uusi()

#Pääohjelman while-loop
    while True:

#Muistikirjan vaihtoehdot ja kysely mitä halutaan tehdä
        print ("Käytetään muistiota: ", muistio)
        print("""(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta""")

        kysely = int(input("Mitä haluat tehdä?: "))

#1 Tulostaa kirjoitetut tiedot
        if kysely == 1:
            tiedosto = open(muistio, "r")
            print (tiedosto.read())

            tiedosto.close()

#2 Lisää merkinnän muistikirjaan ja aikaleiman
        elif kysely == 2:

            teksti = input("Kirjoita uusi merkintä: ")

            tiedosto = open(muistio, "a", )
            tiedosto.write(teksti)
            tiedosto.write(":::")
            tiedosto.write(time.strftime("%X %x"))
            tiedosto.write("\n")
            tiedosto.close()

#3 Tyhjentää muistikirjan tyhjäksi

        elif kysely == 3:
            tiedosto = open(muistio, "w")
            tiedosto.close()
            print ("Muistio tyhjennetty.")

#4 Vaihtaa muistiota toiseen
        elif kysely == 4:
            muistio = input("Anna tiedoston nimi: ")
            tiedosto = open(muistio, "w")
            print ("Tiedostoa ei löydy, luodaan tiedosto.")

    #5 Lopettaa ohjelman       
        if kysely == 5:
            print ("Lopetetaan.")
            break

if __name__ == "__main__":
        main()