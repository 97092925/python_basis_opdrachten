import math

def kubus_vol(a):
    volume = a ** 3  
    return volume

def bol_vol(r):
    volume = (4/3) * math.pi * (r ** 3)  
    return volume

kubus_zijde = 5
bol_straal = 4

kubus_volume = kubus_vol(kubus_zijde)
bol_volume = bol_vol(bol_straal)

print(f"De inhoud van deze kubus is: {kubus_volume}")
print(f"De inhoud van deze bol is: {bol_volume}")