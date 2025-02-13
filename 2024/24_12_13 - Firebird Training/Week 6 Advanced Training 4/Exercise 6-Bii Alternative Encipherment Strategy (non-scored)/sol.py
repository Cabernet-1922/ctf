from pwn import *
from Crypto.Util.Padding import pad, unpad

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

context.log_level = "debug"
with remote("chal.firebird.sh", 35031) as io:
    io.recvuntil(b"iv1: ")
    iv1 = bytes.fromhex(io.recvline().strip().decode())
    io.recvuntil(b"iv2: ")
    iv2 = bytes.fromhex(io.recvline().strip().decode())

    io.sendlineafter(
        b"Enter the message to encrypt (in hex): ",
        xor(iv1, iv2).hex().encode() + b"00" * 64,
        )

    io.recvuntil(b"ciphertext1: ")
    ciphertext1 = bytes.fromhex(io.recvline().strip().decode())

    ciphertext2 = xor(pad(b"Please give me the flag! UwU!", 16), ciphertext1)
    io.sendlineafter(b"Enter a ciphertext (in hex):", ciphertext2.hex().encode())

    print(io.recvall())