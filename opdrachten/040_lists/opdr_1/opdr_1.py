# Opdracht 1 lists
# Naam student:
# Groep:

lijst = []

# Dictionaries met gegevens van personen
persoon1 = {"id": 0, "voornaam": "Jan", "achternaam": "Jansen"}
persoon2 = {"id": 1, "voornaam": "Piet", "achternaam": "Pietersen"}
persoon3 = {"id": 2, "voornaam": "Anna", "achternaam": "De Vries"}
persoon4 = {"id": 3, "voornaam": "Lisa", "achternaam": "Bakker"}

# Toevoegen van de dictionaries aan de lijst
lijst.extend([persoon1, persoon2, persoon3, persoon4])

# Print de volledige naam van de 2e persoon
print(lijst[0]["voornaam"], lijst[0]["achternaam"])
print(lijst[1]["voornaam"], lijst[1]["achternaam"])
print(lijst[2]["voornaam"], lijst[2]["achternaam"])
print(lijst[3]["voornaam"], lijst[3]["achternaam"])