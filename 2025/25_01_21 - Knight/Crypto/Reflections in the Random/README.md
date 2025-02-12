```python
def xor(a, b) -> bytes:
    return bytes(b ^ j for j in a)


chipher = "PzExcRcFHQsdOxF2cR0WEXIPOQQWAQk="
key = 0x42

import base64
plaintext = xor(base64.b64decode(chipher),key).decode()
print(plaintext[::-1])
```
flag: `KCTF{M0ST_34Sy_I_GU3ss}`