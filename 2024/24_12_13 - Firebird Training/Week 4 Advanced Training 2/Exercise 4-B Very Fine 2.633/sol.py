from pwn import *
from Crypto.Util.number import long_to_bytes, isPrime

r = remote('chal.firebird.sh', 35023,level="CRITICAL")

r.recvuntil(b'find the secret below\r\n')
secret = r.recvline()
r.recvuntil(b'> ')
r.sendline(b'1')
result1 = r.recvline()
r.recvuntil(b'> ')
r.sendline(b'-1')
result2 = r.recvline()
r.close()

secret = int(secret[:-2],16)
a_plus_b_mod_p = int(result1[:-2],16)
neg_a_plus_b_mod_p = int(result2[:-2],16)

for b_mod_p in range(32*32):
    a_mod_p = a_plus_b_mod_p - b_mod_p
    p = abs(a_plus_b_mod_p - neg_a_plus_b_mod_p - 2*a_mod_p)
    if isPrime(p):
        for k in range(10):
            m = (secret-b_mod_p)*pow(a_mod_p,-1,p) % p + k*p
            flag = long_to_bytes(m)
            if b'flag{' in flag:
                print(flag.decode())
                break