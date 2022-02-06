"""
Kurssin viimeinen proseduraaliseen ohjelmointiin liittyvä tehtävä on eräänlainen päättötyö, joka kokoaa kaikki kurssilla käsitellyt asiat yhteen kokonaisuuteen. Tässä tehtävässä muokataan muistikirja-harjoitustehtävää viimeisen kerran. Koska ohjelman rakenne muuttuu melko paljon, myös "puhtaalta pöydältä" aloittaminen on ihan järkevä vaihtoehto.

 

Työssä rakennetaan muistikirja, joka käyttää merkintöjen hallintaan Pythonin lista-tietorakennetta sekä tallentaa muistikirjan bittimuotoisena tietokoneen levylle. Ohjelmassa on seuraavat ominaisuudet:
A) Ohjelmaan voidaan lisätä merkintöjä, joissa on samanlainen aikaleima kuin aiemmin.
B)Ohjelmassa voi valita merkinnän listalta, ja korvata sen uudella.
C)Ohjelmalla voi poistaa yksittäisen merkinnän listalta, sekä
D)Ohjelma lataa aiemmin luodun listan ohjelman käynnistyessä mikäli sellainen on olemassa.

 

Ohjelma käyttää tietokantanaan tiedostoa nimeltä "muistio.dat". Käynnistyessään ohjelma koittaa ladata aiemmin luodun listan ko. tiedostosta, tai mikäli tällaista ei ole olemassa tai sen lataaminen tuottaa virheen, luo uuden ilmoittaen "Virhe tiedostossa, luodaan uusi muistio.dat.". Tämän jälkeen käyttäjä voi lisätä merkintljä listalle kuten aiemmin:

 

Virhe tiedostossa, luodaan uusi muistio.dat.
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta kananmunia
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta perunoita

 

Käyttäjä voi myös halutessaan muuttaa yksittäistä merkintää valinnalla 3. Tämän jälkeen ohjelma ilmoittaa listalla olevien merkintöjen määrän "Listalla on [määrä] merkintää." Pyytää käyttäjältä muutettavan merkinnän numeron "Mitä niistä muutetaan?:". Käyttäjä ilmoittaa haluamansa luvun ja voi tämän jälkeen vaihtaa tekstin ja saa uuden aikamerkinnän. Huomaa, että pyydettäessä numeroa ohjelma ymmärtää luvun 1 tarkoittavan ensimmäistä merkintää eli listan alkiota [0].

 

(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 3
Listalla on 2 merkintää.
Mitä niistä muutetaan?: 1
-Osta kananmunia:::14:52:54 01/04/09
Anna uusi teksti: -Osta tärpättiä

 

Tietueen poisto listalta toimii samalla tavalla kuin muokkaus. Ainoa ero on siinä, että ohjelma tulostaa käyttäjälle tiedon siitä, mikä merkintä listalta poistettiin tulosteella "Poistettiin merkintä [merkintä]".

 

(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 4
Listalla on 2 merkintää.
Mitä niistä poistetaan?: 2
Poistettiin merkintä -Osta perunoita:::14:53:00 01/04/09

 

Lopuksi käyttäjän lopettaessa listalla olevat merkinnät tallennetaan pickle-moduulia apunakäyttäen tiedostoon "muistio.dat" ja tulostaa "Lopetetaan.".

 

(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 5
Lopetetaan.

 

Jos ohjelma käynnistetään uudelleen, ladataan aiemmalla käyttökerralla luodut merkinnät tiedostosta "muistio.dat", jolloinka niitä voidaan käyttää myös toisella käyttökerralla. Lisäksi, jos käyttäjä haluaa lukea muistikirjaa, tulostaa ohjelma listan alkiot allekkain:

 

(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 1
-Osta tärpättiä:::14:53:16 01/04/09
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 5
Lopetetaan.

 

Ohjelma on monimutkaisempi kuin useimmat tähänasti käsitellyt esimerkit, mutta se on mahdollista toteuttaa n. 50-60 rivillä koodia tämän kurssin ohjeita hyödyntäen. Kun saat ohjelman toimimaan, voit onnitella itseäsi koska olet ymmärtänyt ja oppinut hyödyntämään tämän kurssin kaikkia pääaiheita!

 

Vinkki: Aikaleiman saa komennolla

import time
aikaleima = time.strftime("%X %x")


"""
import pickle
import time

def lue_tiedosto(tiedostonimi):

    while True:
        try:
            avaus = open(tiedostonimi, "rb")
            tiedosto = pickle.load(avaus)
            avaus.close()
            return tiedosto

        except IOError:
            print ("Virhe tiedostossa, luodaan uusi muistio.dat.")
            uusi_avaus = open(tiedostonimi, "wb")
            lista = []
            pickle.dump(lista, uusi_avaus)
            uusi_avaus.close()


def main():
   
    lista = []
    tiedostonimi = "muistio.dat"
    lista = lue_tiedosto(tiedostonimi)

    while True:

            print("""(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta
""")

            komento = int(input("Mitä haluat tehdä?:"))
#1: Tulostaa muistioon kirjoitetut tiedot
            if komento == 1: 
                for i in lista:
                    print (i)

#2: Lisää merkinnän ja aikaleiman muistioon string-muodossa
            elif komento == 2:
                teksti = input ("Kirjoita uusi merkintä:") 
                lista.append(str(teksti + ":::" + time.strftime("%X %x")))

#3: Kertoo merkintöjen määrän ja muokkaa haluttua merkintää
            elif komento == 3:
                #tiedosto = open(muistio, "wb")
                print ("Listalla on", len(lista), "merkintää.")
                valinta = ((int(input("Mitä niistä muutetaan?: "))) -1)
                print (lista[valinta])
                teksti = input ("Anna uusi teksti:")
                lista[valinta] = str(teksti + ":::" + time.strftime("%X %x"))
                
#4: Poistaa halutun merkinnän ja tulostaa sen

            elif komento == 4:
                print ("Listalla on", len(lista), "merkintää.")
                poisto = int(input("Mitä niistä poistetaan?:"))
                print ("Poistettiin merkintä", lista[poisto -1])
                lista.pop(poisto -1)

#5: Tallentaa käyttäjän antamat tiedot ja lopettaa ohjelman
            elif komento == 5:
                print("Lopetetaan.")
                kirjoita_tiedosto = open("muistio.dat", "wb")
                pickle.dump(lista,kirjoita_tiedosto)
                kirjoita_tiedosto.close()
                break

if __name__ == "__main__":
    main()