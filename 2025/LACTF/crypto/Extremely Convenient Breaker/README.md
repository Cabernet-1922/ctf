# Extremely Convenient Breaker [232 points] (329 solves)
The flag is encrypted by using `AES.ECB`, as we know it is a block cipher. So we can change the order of the blocks to bypass the restriction, and send to remote server decrypt the flag:
```python
from pwn import *
import re
p = remote("chall.lac.tf",31180)
p.recvline()
flag_enc = p.recvline().decode().strip()
p.recv()
payload = flag_enc[32:]+flag_enc[:32]
p.sendline(payload.encode())
flag = p.recvline().decode().strip()
part2 = re.findall(r'[\w]*\}', flag)[0]
part1 = re.findall(r'lactf\{[\w]*', flag)[0]
print(part1+part2)
```

flag: `lactf{seems_it_was_extremely_convenient_to_get_the_flag_too_heh}`