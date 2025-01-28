# XOR-Dinary [50 points] (194 solves)
Simply bruteforce all the character: 
```python
def xor(a, b) -> bytes:
    return bytes(b ^ j for j in a)

a = bytes.fromhex("4e4f594e5c617763457c2e6c2a282b2d29456d2a287e452b2f45772a2b2f2d67")


for i in range(1,256):
    if b"TUCTF" in xor(a,i):
        print(xor(a,i).decode())
```
flag: `TUCTF{my_f4v02173_w02d_15_m0157}`