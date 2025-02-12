# What a Mystake! (1) [794 points] (6 solves)
```python
import ast
from pwn import *
context.log_level = 'CRITICAL'
p = remote('phoenix-chal.firebird.sh', 36015)
n, e, c = ast.literal_eval(p.recvline().strip().decode().lstrip("n, e, c = "))

p.sendline(str(n).encode())
m1 = int(p.recvline().decode().strip()[4:])

cn = pow(c, n, n)
m0 = m1 * pow(cn, -1, n) % n

p.sendline(str(m0).encode())
print(p.recvline().strip().decode()[4:])
```