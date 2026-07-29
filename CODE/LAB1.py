# Caesar Cipher in Python

def encrypt(text, key):
    cipher = ""
    for ch in text:
        if ch.isupper():
            cipher += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            cipher += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            cipher += ch
    return cipher


def decrypt(cipher, key):
    text = ""
    for ch in cipher:
        if ch.isupper():
            text += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
        elif ch.islower():
            text += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            text += ch
    return text


plain = input("Enter the plain text: ")
key = int(input("Enter the key value: "))

cipher = encrypt(plain, key)
print("Encrypted Text:", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted Text:", decrypted)
