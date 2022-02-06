"""
Luvun kolmannessa tehtävässä puhutaan listasta ja tiedostojen käsittelystä. Meillä on olemassa tiedosto "sanoja.txt", joka sisältää joukon erilaisia sanoja. Tehtävänäsi on lukea sanat muistiin, laittaa ne aakkosjärjestykseen ja tulostaa ruudulle allekkain selitteen "Sanat laitettuna aakkosjärjestykseen:" alle. Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:


Sanat laitettuna aakkosjärjestykseen:
aavikkorotta
autokauppias
hattuteline
huono
kaljakori
kivitalo
kumipallo
lapio
puuveistos
rautanaula
saunatonttu
tuuli



Kaikki sanat alkavat pienellä kirjaimella ja niiden jälkeen on rivinvaihto. Tehtävää varten kannattaa erityisesti tutustua listan metodiin .sort, sekä muistaa rivinvaihtojen poistaminen luetuista sanoista.

"""
#Luodaan lista ja uusi lista muutosta varten
lista = []
uusi_lista = []

#Avataan tekstitiedosto muuttujaan tiedosto
tiedosto = open("sanoja.txt", "r")

#Käydään läpi tiedosto
for x in tiedosto:
    uusi_lista.append(x.strip())

#Lisätään uuteen listaan tiedoston tiedot
uusi_lista += tiedosto

#Järjestetään uusi lista aakkosjärjestykseen
uusi_lista.sort()

#Tulostetaan uusi lista
print ("Sanat laitettuna aakkosjärjestykseen:")
for i in uusi_lista:
    print(i)