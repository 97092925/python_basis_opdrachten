def encrypten(tekst):
    encrypted_text = ""

    for char in tekst:
        if char.isalpha():  # Controleer of het een letter is
            # Bepaal of de letter een kleine letter is
            start = 97 if char.islower() else 65
            # Verschuif de letter 5 posities verder in het alfabet
            encrypted_char = chr((ord(char) - start + 5) % 26 + start)
            encrypted_text += encrypted_char
        else:
            # Voeg niet-alfabetische tekens ongewijzigd toe
            encrypted_text += char

    return encrypted_text

# Vraag de gebruiker om een tekst in te voeren
tekst = input("Geef de tekst die je wilt encrypten: ")

# Encrypt de tekst
encrypted = encrypten(tekst)

# Toon de versleutelde tekst
print("Encrypted tekst:")
print(encrypted)



