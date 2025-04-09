def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        voornaam = naam["voornaam"]
        tussenvoegsel = naam["tussenvoegsel"]
        achternaam = naam["achternaam"]
        
        if tussenvoegsel:
            volledige_naam = f"{voornaam} {tussenvoegsel} {achternaam}"
        else:
            volledige_naam = f"{voornaam} {achternaam}"
        
        print(volledige_naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)