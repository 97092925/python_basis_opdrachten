

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]
keuze = input(f"Kies je topping uit deze lijst: {beschikbare_toppings} \n")
topping_gevonden = False
for topping, prijs in toppings:
    if keuze.lower() == topping:  
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        topping_gevonden = True
        break
if not topping_gevonden:
    print("Uw keuze zit niet in ons assortiment")