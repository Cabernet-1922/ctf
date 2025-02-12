```python
from Crypto.Util.Padding import *
from Crypto.Cipher import AES
from base64 import *

b32 = b32decode("G7G2DGQ5SY4DCK5YVUDRROJI3UOAUUNTVR6XKDOKQO4CAAKK2MJA====")
key = b"0123456789ABCDEF"
iv = b"FEDCBA9876543210"

c = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(b32), 16).decode()[::-1]
print(c)
```
flag: `KCTF{R3vers3_R3vers3_D3C0DE}`
