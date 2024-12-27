# Exercise 8-B Lost my keys [100 points] (27 solves)
```python
from pwn import *
from sympy.ntheory.modular import crt
from Crypto.Util.number import long_to_bytes
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend
from gmpy2 import *

context.log_level = "CRITICAL"
sys.set_int_max_str_digits(0)


def read_n_e(key_pem):
    key = load_pem_public_key(key_pem.encode(), default_backend())
    return key.public_numbers().n, key.public_numbers().e


def get():
    p = remote("chal.firebird.sh", 35044)
    public_key = p.recvuntil(b"-----END PUBLIC KEY-----").decode()
    n, e = read_n_e(public_key)
    ct = p.recvline_startswith(b"The encrypted flag is ").decode().strip("The encrypted flag is ").strip()
    return n, e, int(ct)


n_list, ct_list = [], []
for i in range(17):
    n, e, ct = get()
    n_list.append(n)
    ct_list.append(ct)
m = long_to_bytes(iroot(crt(n_list, ct_list)[0], 17)[0]).decode()
print(m)
```

Message: 
```text
Here is the flag: flag{lUcki1Y_tHe_1S_sMa11_eN0uGh}
The same attack still works for e=65536 given enough time. However for a much larger e this attack will be too slow.
```