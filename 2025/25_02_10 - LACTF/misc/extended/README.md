# extended [188 points] (462 solves)
```python
with open("chall.txt", "rb") as f:
    extended_flag = f.read().decode("iso8859-1")

flag = ""
for c in extended_flag:
    o = bin(ord(c))[2:].zfill(8)
    for i in range(8):
        if o[i] == "1":
            o = o[:i] + "0" + o[i + 1 :]
            break

    flag += chr(int(o, 2))

print(flag)
```

flag: `lactf{Funnily_Enough_This_Looks_Different_On_Mac_And_Windows}`