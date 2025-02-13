from pwn import *
import re
p = remote("chal.firebird.sh",35030,level="CRITICAL")
flag_enc = re.findall("[0-9a-f]{10,}",p.recvline().decode().strip())[0]
p.sendline(flag_enc.encode())
flag_hex = re.findall("[0-9a-f]{10,}",p.recvline().decode().strip())[0]
print(bytes.fromhex(flag_hex).decode())
