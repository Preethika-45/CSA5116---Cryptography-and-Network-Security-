def encrypt(text):
    rail1 = ""
    rail2 = ""

    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]

    return rail1 + rail2

plain = input("Enter Plain Text: ")

cipher = encrypt(plain)

print("Encrypted Text:", cipher)
