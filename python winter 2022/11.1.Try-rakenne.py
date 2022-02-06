"""
Ensimmäinen tehtävä on useampaan kertaan jo vastaantullut merkkijonon kääntäminen kokonaisluvuksi. Tee virheenkorjausrakenne, jossa käyttäjältä pyydetään luku "Anna luku: ", ja mikäli tyyppimuunnos onnistuu, tulostetaan "Syöte oli kelvollinen." ja virheen tapahtuessa "Virheellinen syöte!". Ohjelma tulostaa toimiessaan seuraavaa:


Anna luku: Apina
Virheellinen syöte!



tai vaihtoehtoisesti


Anna luku: 234
Syöte oli kelvollinen.



Virheiden kiinniottoon sopivin luokka on tässä tehtävässä yleisluokka "Exception". Lisäksi tulostuksessa kannattaa tutustua siihen, kuinka try-rakenteen else-osio toimii.

"""
# -*- coding: cp1252 -*-

testi = (input("Anna luku: "))

try:
    testi = int(testi)
    print ("Syöte oli kelvollinen.")

except Exception:
    print ("Virheellinen syöte!")