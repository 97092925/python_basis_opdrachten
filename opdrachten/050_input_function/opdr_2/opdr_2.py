# Stap 1: Maak de gastenlijst
lijst = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print(lijst)

# Stap 2: Verwijder Marie uit de lijst
lijst.remove("Marie")
print(lijst)

# Stap 3: Voeg George toe naast Kees
index_kees = lijst.index("Kees")  # Vind de index van Kees
lijst.insert(index_kees + 1, "George")  # Voeg George toe naast Kees
print(lijst)