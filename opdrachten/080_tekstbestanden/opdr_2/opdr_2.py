import random

def raad_je_getal():
    # Genereer een willekeurig getal tussen 1 en 100
    geheime_getal = random.randint(1, 100)
    pogingen = 0

    print("Raad mijn geheime getal (tussen 1 en 100)!")

    # De gebruiker blijft raden totdat het juiste getal is geraden
    while True:
        try:
            # Vraag de gebruiker om een getal in te voeren
            gok = int(input("Voer een getal in: "))
        except ValueError:
            print("Voer alstublieft een geldig getal in!")
            continue

        pogingen += 1

        # Controleer of het getal te hoog, te laag of juist is
        if gok < geheime_getal:
            print("Hoger!")
        elif gok > geheime_getal:
            print("Lager!")
        else:
            # Het juiste getal is geraden
            print(f"Je hebt het getal geraden! Het is {geheime_getal}.")
            print(f"Je hebt {pogingen} keer geraden.")
            break

# Start het spel
if __name__ == "__main__":
    raad_je_getal()

