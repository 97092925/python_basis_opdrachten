def write_to_file(bestandsnaam, tekst):
    # Open het bestand in 'append' modus, zodat we tekst toevoegen zonder het bestand te overschrijven
    with open(bestandsnaam, "a") as bestand:
        bestand.write(tekst + "\n")  # Voeg een nieuwe regel toe na de tekst

# Voorbeeld van het gebruik van de functie
my_tekst = "test bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
