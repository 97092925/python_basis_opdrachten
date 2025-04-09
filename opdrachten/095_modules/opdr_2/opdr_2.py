# Zelfgemaakte module importeren (csv.py) uit de map 'my_modules'
from my_modules import csv

# Voorbeeldlijst van mensen met gegevens zoals voornaam, achternaam, plaats, enz.
personen = [
    {"voornaam": "Jan", "tussenvoegsel": "van der", "achternaam": "Vliet", "plaats": "Amsterdam"},
    {"voornaam": "Piet", "tussenvoegsel": "", "achternaam": "De Vries", "plaats": "Den Haag"},
    {"voornaam": "Griet", "tussenvoegsel": "van der", "achternaam": "Pol", "plaats": "Utrecht"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Siewers", "plaats": "Groningen"},
    {"voornaam": "Jan", "tussenvoegsel": "Jaap", "achternaam": "Siewers", "plaats": "Leiden"},
]

# Functie om te filteren op basis van een veld en waarde
def filter(persoon, filterveld, filterterm):
    # Itereer door de lijst van personen en print degene die voldoen aan de filter
    for p in persoon:
        if p[filterveld].lower().startswith(filterterm.lower()):  # Vergelijken zonder hoofdlettergevoeligheid
            volledige_naam = f"{p['voornaam']} {p['tussenvoegsel']} {p['achternaam']}".strip()
            print(volledige_naam)

# Test de filterfunctie
print("Filter op voornaam met 'Ja':")
filter(personen, "voornaam", "Ja")

print("\nFilter op voornaam met 'Pie':")
filter(personen, "voornaam", "Pie")

print("\nFilter op plaats met 'd':")
filter(personen, "plaats", "d")