# Loginator [97 points] (143 solves)
Easy bruteforce:
```python
import os

a = "02 92 a8 06 77 a8 32 3f 15 68 c9 77 de 86 99 7d 08 60 8e 64 77 be ba 74 26 96 e7 4e"
res = ""

strings_ = a.split(" ")
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}~_!?"
for i in strings_:
    for char in character:
        k = os.popen(f"./loginator.out '{res + char}'").read().strip()
        if k.split(" ")[-1] == i:
            res += char
            print(res)
            break
```

flag: `BITSCTF{C4ND4C3_L0G1C_W0RK?}`