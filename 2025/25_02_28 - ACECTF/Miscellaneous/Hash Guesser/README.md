# Hash Guesser [300 points] (43 solves)
Bruteforce every position of the MD5 hash:
```python
from pwn import *

p = remote("34.131.133.224",5000)
context.log_level = "CRITICAL"
res = ""
hex_set = "0123456789abcdef"
for count in range(1,33):
    for i in hex_set:
        p = remote("34.131.133.224",5000)
        p.sendline((res+str(i)).ljust(32,"0"))
        if f"{count}/32" in p.recvall().decode():
            res += str(i)
            print(res)
            break
        p.close()

print(res)

# 88ef3cb6cbe5d99e6fee9f1e5cb248ba
```
After bruteforce all position, the correct MD5 hash is printed: `88ef3cb6cbe5d99e6fee9f1e5cb248ba`. Submit the hash to remote server to get the flag.

flag: `ACECTF{h45h_cr4ck1n6_r3qu1r35_4_l177l3_w17}`