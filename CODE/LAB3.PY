def generate_key(text, key):
    key = key.upper()
    text = text.upper()
    new_key = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            new_key += key[j % len(key)]
            j += 1
        else:
            new_key += ch
    return new_key


def encrypt(text, key):
    text = text.upper()
    key = generate_key(text, key)
    cipher = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26
            cipher += chr(x + ord('A'))
        else:
            cipher += text[i]

    return cipher


def decrypt(cipher, key):
    cipher = cipher.upper()
    key = generate_key(cipher, key)
    plain = ""

    for i in range(len(cipher)):
        if cipher[i].isalpha():
            x = (ord(cipher[i]) - ord(key[i])) % 26
            plain += chr(x + ord('A'))
        else:
            plain += cipher[i]

    return plain


plaintext = input("Enter Plain Text: ")
key = input("Enter Key: ")

cipher = encrypt(plaintext, key)
print("Encrypted Text:", cipher)

plain = decrypt(cipher, key)
print("Decrypted Text:", plain)
