import math

# Vraag de gebruiker om de lengte van de eerste en tweede zijde
zijde1 = float(input("Geef de lengte van de eerste zijde\n"))
zijde2 = float(input("Geef de lengte van de tweede zijde\n"))

# Bereken de schuine zijde met de stelling van Pythagoras
schuine_zijde = math.sqrt(zijde1**2 + zijde2**2)

# Print de lengte van de schuine zijde
print(f"\nDe lengte van de schuine zijde is: {schuine_zijde}")


