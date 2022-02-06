"""
Toisessa tehtävässä kirjoitetaan tiedostoon. Tee ohjelma, joka ensin pyytää käyttäjältä tiedoston nimen, ja tämän jälkeen tekstin, jonka käyttäjä haluaa tiedostoon kirjoitettavan. Tämän jälkeen ohjelma tekee tiedoston, kirjoittaa tuloksen ja antaa ilmoituksen "Luotiin tiedosto [tiedostonnimi] ja siihen tallennettiin teksti: [sisältö]." Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavan tekstin:


Minkäniminen tiedosto luodaan?: loki.txt
Mitä kirjoitetaan tiedostoon?: Attencion, attencion. 10, 10, 22, 33, Adios.
Luotiin tiedosto loki.txt ja siihen tallennettiin teksti: Attencion, attencion. 10, 10, 22, 33, Adios.
"""

#Kysyy luotavan tiedoston nimen ja luo sen
nimi = input("Minkäniminen tiedosto luodaan?: " )

tiedosto = open(nimi, "x")

#Kysyy mitä halutaan tiedostoon kirjoitettavan
teksti = input("Mitä kirjoitetaan tiedostoon?: ")

tiedosto.write(teksti)

#Sulkee tiedoston
tiedosto.close()

print ("Luotiin tiedosto", nimi, "ja siihen tallennettiin teksti: ", teksti)