def verzamel_gegevens():
    vragen = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]
    
    feestganger = {}

    # Stel de vragen en sla de antwoorden op
    for i, vraag in enumerate(vragen):
        antwoord = input(f"{i+1}. {vraag}\n")  # Vraag met nummering
        if i == 0:
            feestganger['voornaam'] = antwoord
        elif i == 1:
            feestganger['achternaam'] = antwoord
        elif i == 2:
            feestganger['drank'] = antwoord
        elif i == 3:
            feestganger['eten'] = antwoord
    
    # Toon dankbericht
    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")
    
    # Schrijf de gegevens naar een bestand
    with open("feestganger_data.txt", "a") as bestand:
        bestand.write("----\n")
        for sleutel, waarde in feestganger.items():
            bestand.write(f"{sleutel}: {waarde}\n")

# Vraag of de gebruiker meerdere feestgangers wil invoeren
while True:
    verzamel_gegevens()
    
    meer_feestgangers = input("\nWil je nog een feestganger toevoegen? (ja/nee): ").strip().lower()
    if meer_feestgangers != "ja":
        break