import string

alphabet = string.ascii_uppercase
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

plain = input("Enter the plain text: ").upper()

# Encryption
cipher = ""
for ch in plain:
    if ch.isalpha():
        index = alphabet.index(ch)
        cipher += key[index]
    else:
        cipher += ch

print("Encrypted Text:", cipher)

# Decryption
decrypted = ""
for ch in cipher:
    if ch.isalpha():
        index = key.index(ch)
        decrypted += alphabet[index]
    else:
        decrypted += ch

print("Decrypted Text:", decrypted)
