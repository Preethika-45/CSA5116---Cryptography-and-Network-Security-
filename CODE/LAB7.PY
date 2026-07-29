import math

text = input("Enter Plain Text: ").replace(" ", "").upper()
key = input("Enter Key: ").upper()

col = len(key)
row = math.ceil(len(text) / col)

fill = row * col - len(text)
text += "X" * fill

matrix = []

k = 0
for i in range(row):
    matrix.append(list(text[k:k + col]))
    k += col

order = sorted(list(enumerate(key)), key=lambda x: x[1])

cipher = ""

for index, _ in order:
    for r in matrix:
        cipher += r[index]

print("Encrypted Text:", cipher)
