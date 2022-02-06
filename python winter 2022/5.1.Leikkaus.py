"""
Luvun viimeisessä tehtävässä kokeillaan merkkijonon leikkaamista. Määrittele muuttuja, joka sisältää merkkijonon "Hattukauppias". Tämän jälkeen ota siitä leikkaukset, joissa on A)neljä ensimmäistä kirjainta B) neljä viimeistä kirjainta ja C) merkkijono väärinpäin. Tulosta vastaus muodossa


Muuttujan 4 ensimmäistä kirjainta ovat Hatt
Muuttujan 4 viimeistä kirjainta ovat pias
Muuttujan teksti on väärinpäin saippuakuttaH
"""

muuttuja = "Hattukauppias"

print ("Muuttujan 4 ensimmäistä kirjainta ovat", muuttuja [:4])
print ("Muuttujan 4 viimeistä kirjainta ovat", muuttuja [-4:])
print ("Muuttujan teksti on väärinpäin", muuttuja [::-1])