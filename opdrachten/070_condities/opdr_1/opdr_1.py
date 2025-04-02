# Maak een lege lijst
getallen = []

# Vul de lijst met getallen van 1 t/m 10
for i in range(1, 11):
    getallen.append(i)

# Print alleen de getallen die groter zijn dan 4
for getal in getallen:
    if getal > 4:
        print(getal)