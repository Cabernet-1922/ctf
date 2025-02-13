key = list(bytearray.fromhex("3da4e514c6f9c8239b9ac1204e0d422d"))
iv = list(bytearray.fromhex("064209f2b4f7aa65a6f53c7267bdd4df"))
thing = list(bytearray.fromhex("5d8a8d81094757190a07cc217683e0972713401648b0fdbb4116a20f2bd677009230db8c8990b3b6033b9fabcec2b1f908f1fbc284d29e8ba7de8b6d370a9262"))

dec = []

for j in range(9):
    temp = key[0]
    for k in range(1, len(key)):
        key[k - 1] = key[k]
    key[len(key) - 1] = temp

# print(thing, key, iv)
for i in range(3, -1, -1):
    t = thing[i * 16:(i + 1) * 16]
    d = thing[(i - 1) * 16:i * 16]
    if d == []:
        d = iv
    t = [a ^ b ^ c for a, b, c in zip(key, t, d)]
    for j in range(3):
        temp = key[len(key) - 1]
        for k in range(len(key) - 2, -1, -1):
            key[k + 1] = key[k]
        key[0] = temp
    dec.append(t)

for i in dec[::-1]:
    for j in i:
        print(chr(j), end="")