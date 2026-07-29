key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

text = input("Enter Plain Text (3 letters): ").upper()

while len(text) < 3:
    text += "X"

text = text[:3]

P = [ord(ch) - 65 for ch in text]

C = []

for i in range(3):
    total = 0
    for j in range(3):
        total += key[i][j] * P[j]
    C.append(total % 26)

cipher = ""

for num in C:
    cipher += chr(num + 65)

print("Encrypted Text:", cipher)
