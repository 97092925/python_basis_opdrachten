

import csv

# Functie om een lijst van dictionaries naar een CSV-bestand te schrijven
def schrijf_csv(bestandsnaam, data):
    # Open het CSV-bestand in schrijfmodus
    with open(bestandsnaam, mode='w', newline='', encoding='utf-8') as bestand:
        writer = csv.DictWriter(bestand, fieldnames=data[0].keys())
        writer.writeheader()  # Schrijf de header (de veldnamen)
        writer.writerows(data)  # Schrijf de gegevens
    print(f"Data is succesvol naar {bestandsnaam} geschreven.")

    # Importeer de module csv die we hebben gemaakt in de my_modules map
from my_modules import csv

# Voorbeeldgegevens (lijst van dictionaries)
data = [
    {"naam": "Jan", "leeftijd": 25, "beroep": "Programmeer"},
    {"naam": "Marie", "leeftijd": 30, "beroep": "Ontwerper"},
    {"naam": "Klaas", "leeftijd": 22, "beroep": "Student"}
]

# Roep de functie aan uit de csv module om de gegevens naar een CSV-bestand te schrijven
bestandsnaam = "gegevens.csv"
csv.schrijf_csv(bestandsnaam, data)