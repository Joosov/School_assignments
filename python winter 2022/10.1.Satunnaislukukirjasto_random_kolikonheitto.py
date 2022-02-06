"""
Luvun ensimmäinen tehtävä perustuu random-moduulikirjaston toimintaan. Tee ohjelma, joka arpoo viisi kertaa joko luvun 0 tai 1 käyttäen random.randint-kirjastofunktiota. Mikäli ohjelma arpoo luvun 0, tulostetaan "Klaava!", mikäli 1 niin "Kruuna!". Ohjelma alkaa tulosteella "Heitetään kolikkoa viidesti:" ja toimii seuraavalla tavalla:


Heitetään kolikkoa viidesti:
Klaava!
Kruuna!
Kruuna!
Kruuna!
Kruuna!



Tietenkin tulee muistaa, että satunnaislukuja käytettäessä tulos voi olla mitä tahansa, toisella ajokerralla saatiin esimerkiksi vastaus:


Heitetään kolikkoa viidesti:
Kruuna!
Klaava!
Klaava!
Kruuna!
Klaava!
"""

import random


print ("Heitetään kolikkoa viidesti:")

for i in range(5):
    kolikko = random.randint(0,1)

    if (kolikko == 0):
        print ("Klaava!")
    else: 
        print ("Kruuna!")
