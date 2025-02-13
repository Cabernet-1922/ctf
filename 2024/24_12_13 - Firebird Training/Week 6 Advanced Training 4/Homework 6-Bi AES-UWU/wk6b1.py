from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
import string
import os
from pwn import *

HOST = 'chal.firebird.sh'
PORT = 35032
p = remote(HOST, PORT,level="CRITICAL")
h = p.recvline_contains(b"h = ").strip().decode()[-4:]
# print(h)
p.recv()


# Stage 1
def brute_force_pow(h):
    hex_set = "0123456789abcdef"
    count = 0
    while True:
        count += 1
        length = random.randint(5, 8) * 2
        candidate = "".join(random.choice(hex_set) for _ in range(length))
        padded_candidate = pad(candidate.encode(), 16)
        encrypted = AES.new(padded_candidate, AES.MODE_ECB).encrypt(padded_candidate).hex()
        if encrypted[:4] == h and len(candidate) <= 16:
            return candidate

valid_input = brute_force_pow(h)
# print(valid_input)
p.sendline(valid_input.encode())


# Stage 2
p.recvline()
enc_flag = p.recvline().strip().decode()
enc_flag = bytes.fromhex(enc_flag)
# print("enc_flag: ",enc_flag)

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def padding_oracle(iv, block):
    known_int = b""
    for i in reversed(range(16)):
        padding = b"\x00" * i + bytes([16 - i] * (16 - i))
        for k in range(256):
            test = b"\x00" * i + bytes([k]) + known_int
            dummy_block = os.urandom(16)
            payload = dummy_block + dummy_block + xor(test, padding) + block
            p.sendline(payload.hex().encode())
        for k in range(256):
            if b":)" in p.recvline():
                known_int = bytes([k]) + known_int
                break
        for j in range(255 - k):
            p.recvline()
    return xor(known_int, iv)

plaintext = b""
iv = enc_flag[:16]
for i in range(16, len(enc_flag), 16):
    block = enc_flag[i:i + 16]
    plaintext += padding_oracle(iv, block)
    # print("plaintext: ",plaintext,"\n")
    iv = xor(iv,block)

print(unpad(plaintext,16).decode())
