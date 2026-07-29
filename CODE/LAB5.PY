def generate_key_table(key):
    key = key.upper().replace("J", "I")
    table = []
    for c in key:
        if c not in table and c.isalpha():
            table.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in table:
            table.append(c)
    return [table[i:i+5] for i in range(0, 25, 5)]

def find(table, ch):
    for i in range(5):
        for j in range(5):
            if table[i][j] == ch:
                return i, j

def encrypt(text, table):
    text = text.upper().replace("J", "I")
    text = "".join(c for c in text if c.isalpha())

    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                pairs.append((a, "X"))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        else:
            pairs.append((a, "X"))
            i += 1

    cipher = ""

    for a, b in pairs:
        r1, c1 = find(table, a)
        r2, c2 = find(table, b)

        if r1 == r2:
            cipher += table[r1][(c1 + 1) % 5]
            cipher += table[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher += table[(r1 + 1) % 5][c1]
            cipher += table[(r2 + 1) % 5][c2]
        else:
            cipher += table[r1][c2]
            cipher += table[r2][c1]

    return cipher

key = input("Enter Key: ")
plain = input("Enter Plain Text: ")

table = generate_key_table(key)

print("Encrypted Text:", encrypt(plain, table))
