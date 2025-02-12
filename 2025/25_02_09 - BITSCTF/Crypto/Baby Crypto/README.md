# Baby Crypto [50 points] (233 solves)
```python
from pwn import *
import re
from Crypto.Util.number import long_to_bytes, inverse

context.log_level = 'CRITICAL'

p = remote("chals.bitskrieg.in", 7000)
n, e, ct = re.findall(r"[\d]+", p.recv().decode().strip())[0:3]
n, e, ct = int(n), int(e), int(ct)
s = 2
ct_new = (ct * pow(s, e, n)) % n
p.sendline(str(ct_new).encode())
pt_new = int(re.findall(r"[\d]+", p.recv().decode().strip())[0])
# 39639837536156593072703000049994066086289431135207913625429785307924943603979635946981909260898213168370823268973219279443746657679296399190096606077830951260950823052936192667655676091351812437731066
s_inv = inverse(s, n)
original_msg = (pt_new * s_inv) % n
flag = long_to_bytes(original_msg).decode()
print(flag)
```

flag: `BITSCTF{r54_0r4acl3_h4s_g0t_t0_b3_0n3_0f_7h3_3as13st_crypt0_1n_my_0p1n10n_74b15203}`