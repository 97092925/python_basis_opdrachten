vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]
with open("enquete_resultaten.txt", "w") as bestand:
    for vraag in vragen:
        antwoord = input(vraag + " ")
        bestand.write(f"{vraag}\n{antwoord}\n\n")

