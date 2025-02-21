# Programming Exercise [150 points] (13 solves)
```python
import itertools, ast, concurrent.futures

with open("Generated List.txt") as f:
    res = ast.literal_eval(f.read())

weights = list(range(1, 1000))

def build_inv(key):
    t = [0] * 128
    for x in range(128):
        y = 0
        for j in range(7):
            if x & (1 << key[j]):
                y |= 1 << j
        t[y] = x
    return t

def check_key(candidate):
    t = build_inv(candidate)
    flag_chars = []
    for block in res:
        a = [t[n] for n in block]
        S = sum(w * x for w, x in zip(weights, a[:999])) % 128
        c = S ^ a[999]
        if not (32 <= c < 127):
            return None
        flag_chars.append(chr(c))
    flag = "".join(flag_chars)
    return flag if flag.startswith("flag{") else None

with concurrent.futures.ProcessPoolExecutor() as executor:
    for flag in executor.map(check_key, itertools.permutations(range(7))):
        if flag:
            print("Flag:", flag)
            break
```