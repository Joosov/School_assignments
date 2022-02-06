"""
Kolmas tehtävä käyttää for-toistorakennetta ja se on hieman aiempia monimutkaisempi. Tee ohjelma, joka pyytää käyttäjältä kierrosmäärän. Tämän jälkeen tee ohjelma, joka laskee kierroslukujen kertymän. Eli jos käyttäjä antaa syötteen 3, laskee ohjelma 0+1+2, jos 5 niin 0+1+2+3+4. Lopuksi ohjelma tulostaa käyttäjälle lopputuloksen muodossa "Kertymäksi saatiin:" ja vastaus.

Toimiessaan oikein ohjelma tulostaa seuraavaa:


Kuinka monta kierrosta?: 3
Kertymäksi saatiin: 3



Tehtävässä kannattaa kokeilla kuinka kierrosluvun lisääminen muuttujaan toimii, eli vaikkapa tulos = tulos + kierrosluku.
"""

kierros = int(input("Kuinka monta kierrosta?: "))

tulos = int(0)

for kierros in range (1, kierros):

    tulos = tulos + kierros

print ("Kertymäksi saatiin: ", tulos)