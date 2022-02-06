"""
Toisessa tehtävässä luodaan ostoslista käyttäen Pythonin lista-tietomuotoa. Tee ohjelma, jossa käyttäjä voi (1) lisätä tuotteita listaan, (2) poistaa tuotteita listalta tai (3) lopettaa.

Mikäli käyttäjä lisää tuotteen listaan, pyytää ohjelma syötteen "Mitä lisätään?: ") ja laittaa sen listan viimeiseksi alkioksi. Jos käyttäjä haluaa poistaa tuotteen, kertoo ohjelma "Listalla on [määrä] alkiota", ja käyttäjä antaa syötteen "Monesko niistä poistetaan?", jonka jälkeen ohjelma poistaa numeronmukaisen alkion (0 on siis 1. alkio).

Jos käyttäjä lopettaa, tulostaa ohjelma "Listalla oli tuotteet:" ja listan sisällön kokonaisuudessaan allekkain. Virheelliseen valintaan reagoidaan tulostamalla rivi "Virheellinen valinta". Tämä koskee myös sitä jos käyttäjä valitsee poistettavan alkion listan ulkopuolelta. Toimiessaan ohjelma tulostaa seuraavaa:


Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 1
Mitä lisätään?: Omenoita
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 1
Mitä lisätään?: Olutta
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 2
Listalla on 2 alkiota.
Monesko niistä poistetaan?: 0
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 3
Listalla oli tuotteet:
Olutta



tai vaihtoehtoisesti vaikkapa


Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 2
Listalla on 0 alkiota.
Monesko niistä poistetaan?: 1231
Virheellinen valinta.
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 6
Virheellinen valinta.
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 3
Listalla oli tuotteet:
"""
lista = []
    
while True:

#Tulostetaan vaihtoehdot käyttäjälle
    x =  int(input("""Haluatko
    (1)Lisätä listaan
    (2)Poistaa listalta vai
    (3)Lopettaa?: """))

#Listaan lisäys
    if x == 1:
        syote = input("Mitä lisätään?:")
        lista.append(syote)

#Listan ituus ja poistetaan valittu
    elif x == 2:
        maara = int(len(lista))
        print ("Listalla on", maara, "alkiota.")
        poisto = int(input("Monesko niistä poistetaan?:"))
        
        try:
            lista.pop(poisto)

        except Exception:
            print ("Virheellinen valinta.")

#Tulostaa listan
    elif x == 3:
        print ("Listalla oli tuotteet:")
        for i in lista:
            print(i)
        break

    else:
        print("Virheellinen valinta.")